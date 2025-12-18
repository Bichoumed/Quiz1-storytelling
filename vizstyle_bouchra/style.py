# vizstyle_bouchra/style.py
import matplotlib.pyplot as plt

PALETTE = {
    "ink": "#111827",
    "accent": "#C2410C",
    "accent_dark": "#7C2D12",
    "muted": "#4B5563",
    "light_gray": "#E5E7EB",
    "bg": "#FFFFFF",
}

def apply_style():
    plt.rcParams.update({
        # Figure
        "figure.figsize": (8.5, 5),
        "figure.dpi": 120,
        "figure.facecolor": PALETTE["bg"],
        "axes.facecolor": PALETTE["bg"],

        # Typography
        "font.family": "DejaVu Sans",
        "axes.titleweight": "bold",
        "axes.titlesize": 15,
        "axes.labelsize": 12,
        "axes.titlecolor": PALETTE["ink"],
        "axes.labelcolor": PALETTE["muted"],
        "xtick.color": PALETTE["muted"],
        "ytick.color": PALETTE["muted"],

        # Axes
        "axes.edgecolor": PALETTE["ink"],
        "axes.linewidth": 1.1,

        # No grid
        "axes.grid": False,

        # Lines
        "lines.linewidth": 3.2,
        "lines.solid_capstyle": "round",

        # Legend
        "legend.frameon": False,
    })

    return PALETTE
