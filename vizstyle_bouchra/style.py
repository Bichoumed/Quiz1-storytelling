# vizstyle_bouchra/style.py
import matplotlib.pyplot as plt

PALETTE = {
    "charcoal": "#1F2937",
    "blue": "#2563EB",
    "orange": "#D97706",
    "green": "#15803D",
    "red": "#B91C1C",
    "gray": "#4B5563",
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
        "axes.titlecolor": PALETTE["charcoal"],
        "axes.labelcolor": PALETTE["gray"],
        "xtick.color": PALETTE["gray"],
        "ytick.color": PALETTE["gray"],

        # Axes
        "axes.edgecolor": PALETTE["charcoal"],
        "axes.linewidth": 1.1,

        # NO GRID
        "axes.grid": False,

        # Lines
        "lines.linewidth": 3.2,
        "lines.solid_capstyle": "round",

        # Legend
        "legend.frameon": False,
    })

    return PALETTE
