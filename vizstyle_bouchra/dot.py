# vizstyle_bouchra/dot.py
import matplotlib.pyplot as plt
from .style import apply_style

def styled_dot(x, y, title="", xlabel="", ylabel=""):
    p = apply_style()

    fig, ax = plt.subplots()
    ax.scatter(x, y, s=80, color=p["accent"])

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.show()
