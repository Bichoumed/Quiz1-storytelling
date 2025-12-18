# vizstyle_bouchra/histogram.py
import matplotlib.pyplot as plt
from .style import apply_style

def styled_hist(data, bins=6, title="", xlabel="", ylabel="Frequency"):
    p = apply_style()

    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, color=p["green"], edgecolor=p["charcoal"])

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.show()
