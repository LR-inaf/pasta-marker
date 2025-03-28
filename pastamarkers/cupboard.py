from matplotlib.pyplot import Axes
import numpy as np

# This cupboard contains the toppings for pasta.

def add_parmesan(ax: Axes, amount: int = 10000) -> Axes:
    """Add parmesan to the Axes.
    Parameters:
        ax: Axes
            The Axes to which the parmesan will be added.
        amount: int
            The amount of parmesan to add.
    """
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    _ = ax.scatter(
        np.random.uniform(*xlim, amount),
        np.random.uniform(*ylim, amount),
        marker=".",
        color="white",
        s=3,
    )

    ax.set(xlim=xlim, ylim=ylim)
    return ax
