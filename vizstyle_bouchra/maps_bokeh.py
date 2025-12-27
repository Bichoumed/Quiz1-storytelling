import pandas as pd
import geopandas as gpd

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import (
    GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool,
    Select, CustomJS
)
from bokeh.layouts import column
from bokeh.palettes import Turbo256  # ✅ cool -> hot


def styled_election_map_bokeh_candidate_selector(
    csv_url: str,
    shp_path: str,
    region_col_shp: str = "ADM2_EN",
    region_col_csv: str = "moughataa",
    candidate_col: str = "candidate",
    votes_col: str = "nb_votes",
    title: str = "Election map (ADM2 Moughataa) – select candidate",
    drop_parties: bool = True,
):
    # 1) Load election data
    df = pd.read_csv(csv_url)

    if drop_parties:
        df = df[~df[candidate_col].astype(str).str.contains("Parti", na=False)]

    required = {region_col_csv, candidate_col, votes_col}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}. Available: {list(df.columns)}")

    df[region_col_csv] = df[region_col_csv].astype(str).str.strip()
    df[candidate_col] = df[candidate_col].astype(str).str.strip()
    df[votes_col] = pd.to_numeric(df[votes_col], errors="coerce").fillna(0)

    # 2) Candidate list
    candidates = sorted(df[candidate_col].dropna().unique().tolist())
    if not candidates:
        raise ValueError("No candidates found in CSV after filtering.")
    default_candidate = candidates[0]

    # 3) Winner per moughataa (for hover)
    df_winner = (
        df.sort_values(votes_col, ascending=False)
          .groupby(region_col_csv, as_index=False)
          .first()
          .rename(columns={
              region_col_csv: "region",
              candidate_col: "winner",
              votes_col: "winner_votes",
          })
    )

    # 4) Votes for each candidate per region (wide)
    pivot = (
        df.pivot_table(
            index=region_col_csv,
            columns=candidate_col,
            values=votes_col,
            aggfunc="sum",
            fill_value=0,
        )
        .reset_index()
        .rename(columns={region_col_csv: "region"})
    )

    # 5) Load shapefile
    gdf = gpd.read_file(shp_path)
    required_shp = {region_col_shp, "geometry"}
    missing_shp = required_shp - set(gdf.columns)
    if missing_shp:
        raise ValueError(f"Missing columns in SHP: {missing_shp}. Available: {list(gdf.columns)}")

    gdf = gdf[[region_col_shp, "geometry"]].rename(columns={region_col_shp: "region"})
    gdf["region"] = gdf["region"].astype(str).str.strip()

    # 6) Merge geometry + winner + pivot
    gdf = gdf.merge(df_winner, on="region", how="left")
    gdf = gdf.merge(pivot, on="region", how="left")

    gdf["winner"] = gdf["winner"].fillna("N/A")
    gdf["winner_votes"] = pd.to_numeric(gdf["winner_votes"], errors="coerce").fillna(0)

    for c in candidates:
        if c not in gdf.columns:
            gdf[c] = 0
        gdf[c] = pd.to_numeric(gdf[c], errors="coerce").fillna(0)

    # Selected candidate fields
    gdf["selected_candidate"] = default_candidate
    gdf["selected_votes"] = gdf[default_candidate].astype(float)

    # 7) GeoJSON source
    source = GeoJSONDataSource(geojson=gdf.to_json())

    # 8) ✅ Color scale: low fixed at 0 (calm), high depends on max votes (hot)
    low = 0.0
    high = float(gdf["selected_votes"].max())
    if high <= low:
        high = low + 1.0

    color_mapper = LinearColorMapper(
        palette=Turbo256,   # ✅ cool -> hot
        low=low,
        high=high,
        nan_color="#d9d9d9" # optional: color for missing
    )

    # 9) Figure
    p = figure(
        title=title,
        tools="pan,wheel_zoom,reset,save",
        active_scroll="wheel_zoom",
        width=950,
        height=650,
    )
    p.grid.grid_line_alpha = 0.3

    p.patches(
        "xs", "ys",
        source=source,
        fill_color={"field": "selected_votes", "transform": color_mapper},
        fill_alpha=0.85,
        line_color="white",
        line_width=0.7,
    )

    hover = HoverTool(tooltips=[
        ("Moughataa", "@region"),
        ("Winner", "@winner"),
        ("Winner votes", "@winner_votes{0,0}"),
        ("Selected candidate", "@selected_candidate"),
        ("Selected votes", "@selected_votes{0,0}"),
    ])
    p.add_tools(hover)

    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8)
    p.add_layout(color_bar, "right")

    # 10) Dropdown + JS callback
    selector = Select(title="Choose candidate:", value=default_candidate, options=candidates)

    callback = CustomJS(args=dict(
        source=source,
        selector=selector,
        color_mapper=color_mapper,
    ), code="""
        const geo = JSON.parse(source.geojson);
        const features = geo.features;
        const chosen = selector.value;

        // ✅ keep 0 always the calm color
        let maxV = 0;

        for (let i = 0; i < features.length; i++) {
            const props = features[i].properties;

            let v = props[chosen];
            if (v === null || v === undefined) v = 0;

            props["selected_candidate"] = chosen;
            props["selected_votes"] = v;

            if (v > maxV) maxV = v;
        }

        // ✅ force low=0, update only high
        color_mapper.low = 0;
        color_mapper.high = (maxV > 0) ? maxV : 1;

        source.geojson = JSON.stringify(geo);
    """)

    selector.js_on_change("value", callback)

    show(column(selector, p))
