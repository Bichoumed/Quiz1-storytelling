# vizstyle_bouchra/scatter.py
import matplotlib.pyplot as plt
from .style import apply_style

def styled_scatter(x, y, title="", xlabel="", ylabel=""):
    apply_style()
    plt.scatter(x, y, color="#2ca02c")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()
