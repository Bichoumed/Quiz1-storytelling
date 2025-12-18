# vizstyle_bouchra/bar.py
import matplotlib.pyplot as plt
from .style import apply_style

def styled_bar(x, y, title="", xlabel="", ylabel=""):
    p = apply_style()

    fig, ax = plt.subplots()
    ax.bar(x, y, color=p["orange"], width=0.6)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.show()
