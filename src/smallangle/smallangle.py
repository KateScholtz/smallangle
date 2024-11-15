import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 0,
)
def sin(number):
    """Create a list with NUMBER points between 0 and 2π and the sinus of those points.

    NUMBER is the amount of points in the list.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 0, 
)
def tan(number):
    """Create a list with NUMBER points between 0 and 2π and the tangent of those points.

    NUMBER is the amount of points in the list.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()