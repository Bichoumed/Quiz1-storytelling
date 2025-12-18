# vizstyle_bouchra/boxplot.py
import matplotlib.pyplot as plt
from .style import apply_style

def styled_boxplot(data, title="", ylabel=""):
    p = apply_style()

    fig, ax = plt.subplots()
    ax.boxplot(
        data,
        patch_artist=True,
        boxprops=dict(facecolor=p["blue"], edgecolor=p["charcoal"]),
        medianprops=dict(color=p["charcoal"], linewidth=2),
        whiskerprops=dict(color=p["charcoal"]),
        capprops=dict(color=p["charcoal"]),
    )

    ax.set_title(title)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.show()
