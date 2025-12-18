import vizstyle_bouchra as vz

# 1️⃣ Line plot
vz.styled_line(
    x=[1, 2, 3],
    y=[3, 1, 4],
    title="Styled Line Plot",
    xlabel="X",
    ylabel="Y"
)

# 2️⃣ Bar plot
vz.styled_bar(
    x=["A", "B", "C"],
    y=[5, 2, 7],
    title="Styled Bar Plot",
    xlabel="Category",
    ylabel="Value"
)

# 3️⃣ Scatter plot
vz.styled_scatter(
    x=[1, 2, 3, 4],
    y=[10, 8, 6, 4],
    title="Styled Scatter Plot",
    xlabel="X",
    ylabel="Y"
)

# 4️⃣ Histogram
vz.styled_hist(
    data=[1, 2, 2, 3, 3, 3, 4, 4, 5],
    bins=5,
    title="Styled Histogram",
    xlabel="Values"
)

# 5️⃣ Boxplot
vz.styled_boxplot(
    data=[1, 2, 3, 4, 5, 6, 7],
    title="Styled Boxplot",
    ylabel="Distribution"
)
