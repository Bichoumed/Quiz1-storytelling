# vizstyle_bouchra/scatter.py
import matplotlib.pyplot as plt
from .style import apply_style

def styled_scatter(x, y, title="", xlabel="", ylabel=""):
    p = apply_style()

    fig, ax = plt.subplots()

    # Designer scatter: points pleins + léger contour + transparence
    ax.scatter(
        x, y,
        s=70,                 # taille pro
        color=p["accent"],    # accent unique
        alpha=0.85,           # évite l’effet “blob”
        edgecolors=p["ink"],  # contour fin
        linewidths=0.6
    )

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Clean spines
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    plt.show()
