# vizstyle_bouchra/line.py
import matplotlib.pyplot as plt
from .style import apply_style

def styled_line(x, y, title="", xlabel="", ylabel=""):
    p = apply_style()

    fig, ax = plt.subplots()
    ax.plot(x, y, color=p["blue"], marker="o")

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Clean spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.show()
