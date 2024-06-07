from typing import Optional

import matplotlib as mpl

from cycler import cycler

from qstyles.palettes import Categorical, Diverging, Sequential


def create_palette(palette: str) -> cycler:
    """Helper function to build a repeating list of colors for matplotlib

    Args:
        hex_values (list): A list of hex values for colors to use as a color palette

    Returns:
        cycler: A cycler object that can be used to set the color palette for matplotlib
    """

    sequential_palettes = [
        "violet_light",
        "teal_light",
        "violet_dark",
        "teal_dark",
    ]
    categorical_palettes = [
        "cat_colorful_dark",
        "cat_colorful_light",
        "cat_qs_dark",
        "cat_qs_light",
        "cat_bright",
    ]
    diverging_palettes = ["plum_green", "green_violet"]

    if palette in diverging_palettes:
        hex_values = getattr(Diverging, palette)

    elif palette in categorical_palettes:
        hex_values = list(getattr(Categorical, palette).values())

    elif palette in sequential_palettes:
        hex_values = getattr(Sequential, palette)

    return cycler("color", hex_values)


def set_theme(theme_params: dict) -> None:
    """Pass a dict of style params to matplotlib.

    Args:
        theme_params (dict): style params used to override matplotlib.rcParams
    """
    mpl.rcParams.update(theme_params)


def compose_theme(
    style: str,
    theme_dict: dict,
    grid: bool,
    palette: Optional[str],
    context: Optional[str] = "notebook",
) -> dict:
    """Create a custom matplotlib theme. This method will set the color palette
    and context for the theme.

    Args:
        style (str): One of "light" or "dark"
        theme_dict (dict): Dictionary containing matplotlib style params,
            this is automatically generated.
        palette (Optional[str]): Colour palette to use. Defaults to None.
        context (Optional[str]): Context to use - this will be used to scale
            fonts, line attributes, and paddings should be one of "notebook",
            "print", or "presentation". Defaults to "notebook".

    """

    if palette:
        color_palette = create_palette(palette)
    else:
        palette = f"purple_{style}"
        color_palette = getattr(Sequential, palette)

    # custom_cycler = cycler(color=color_palette) +
    # cycler(marker=['o', 'D', 'v', 's', 'o', 'D'],
    # linestyle=['-', '--', ':', '-.', '-', '--'])

    palette = {
        "axes.prop_cycle": cycler(color=color_palette),
    }

    theme_dict.update(palette)
    theme_dict.update(plotting_context(context))

    # set grid on or off
    if grid:
        theme_dict.update(
            {
                "axes.grid": True,
            }
        )
    else:
        theme_dict.update(
            {
                "axes.grid": False,
            }
        )

    return theme_dict


def plotting_context(
    context: Optional[str] = "notebook", font_scale: float = 1
) -> dict:
    """
    Get the parameters that control the scaling of plot elements.

    These parameters correspond to label size, line thickness, etc.

    The base context is "notebook", and the other contexts are "print" and
    "presentation" which scale the styling from the base notebook context.

    Args:

        context : None, or one of "print, notebook, presentation"
            A dictionary of parameters or the name of a preconfigured set.
        font_scale (float): Separate scaling factor to independently scale
            the size of the text elements.

    """
    if context is None:
        context_dict = {k: mpl.rcParams[k] for k in _context_keys}
    else:
        contexts = ["print", "notebook", "presentation"]
        if context not in contexts:
            raise ValueError(f"context must be one of {', '.join(contexts)}")

        # set up dictionaries of default parameters
        font_base_context = {
            "font.size": 14,
            "axes.titlepad": 16.0,
        }

        base_context = {
            "axes.linewidth": 1.0,
            "grid.linewidth": 0.75,
            "lines.linewidth": 1.5,
            "lines.markersize": 6,
            "patch.linewidth": 1,
            "hatch.linewidth": 1.0,
            "xtick.major.width": 1.0,
            "ytick.major.width": 1.0,
            "xtick.minor.width": 0.75,
            "ytick.minor.width": 0.75,
            "xtick.major.size": 6,
            "ytick.major.size": 6,
            "xtick.minor.size": 4,
            "ytick.minor.size": 4,
        }

        # scale all the parameters by the same factor depending on the context
        scaling = {"print": 0.8, "notebook": 1, "presentation": 1.5}[context]
        context_dict = {k: v * scaling for k, v in base_context.items()}

        # independently scale the fonts and padding
        context_dict["font.size"] = (
            scaling * font_base_context["font.size"] * font_scale
        )
        context_dict["axes.titlepad"] = font_base_context["font.size"] * 1.2

    return context_dict


_context_keys = [
    "font.size",
    "axes.labelsize",
    "axes.titlesize",
    "xtick.labelsize",
    "ytick.labelsize",
    "legend.fontsize",
    "legend.title_fontsize",
    "axes.linewidth",
    "grid.linewidth",
    "lines.linewidth",
    "lines.markersize",
    "patch.linewidth",
    "xtick.major.width",
    "ytick.major.width",
    "xtick.minor.width",
    "ytick.minor.width",
    "xtick.major.size",
    "ytick.major.size",
    "xtick.minor.size",
    "ytick.minor.size",
]
