import vizstyle_bouchra as vz

vz.styled_bar(
    x=["A", "B", "C"],
    y=[5, 2, 7],
    title="Bar Chart",
    xlabel="Category",
    ylabel="Value"
)

vz.styled_scatter(
    x=[1, 2, 3, 4],
    y=[10, 8, 6, 4],
    title="Scatter Plot",
    xlabel="X",
    ylabel="Y"
)

vz.styled_hist(
    data=[1, 2, 2, 3, 3, 3, 4, 4, 5],
    title="Histogram",
    xlabel="Values"
)

vz.styled_boxplot(
    data=[1, 2, 3, 4, 5, 6, 7],
    title="Boxplot",
    ylabel="Distribution"
)

vz.styled_dot(
    x=[1, 2, 3],
    y=[3, 1, 4],
    title="Dot Plot",
    xlabel="X",
    ylabel="Y"
)
