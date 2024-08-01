# Copyright 2024 Quansight Labs. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from pathlib import Path
from typing import Optional

from matplotlib import font_manager

from qstyles.palettes import Base
from qstyles.styler import compose_theme, set_theme


# Vendored font, the user can keep using their own font as per
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/font_family_rc.html
FONTS_PATH = Path(__file__).parent / "vendor/Inter"

font_files = font_manager.findSystemFonts(fontpaths=str(FONTS_PATH))

for font_file in font_files:
    font_manager.fontManager.addfont(font_file)


def _base_theme() -> dict:
    """Common plotting settings for this package. It provides a consistent set
    of plotting settings for all the themes.

    Returns:
        dict: Dictionary containing the common plotting settings and usable by
        matplotlib.rcParams.update()
    """

    style_dict = {
        "font.family": ["sans-serif"],
        "font.sans-serif": ["Inter", "Helvetica", "sans-serif"],
        "axes.titleweight": "bold",
        "axes.labelpad": 8.0,
        "axes.labelweight": 600,
        "axes.labelsize": "medium",
        "axes.titlesize": "x-large",
        "axes.grid.which": "major",
        "xtick.labelsize": "small",
        "ytick.labelsize": "small",
        "xtick.major.size": 8.25,
        "xtick.minor.size": 4.125,
        "xtick.major.pad": 6,
        "xtick.minor.pad": 6,
        "xtick.direction": "out",
        "xtick.minor.visible": False,
        "ytick.major.pad": 6,
        "ytick.minor.pad": 6,
        "ytick.direction": "out",
        "ytick.minor.visible": False,
        "grid.alpha": 0.75,
        "grid.linestyle": ":",
        "legend.fontsize": "small",
        "legend.title_fontsize": "medium",
        "legend.fancybox": True,
        "legend.frameon": True,
        "legend.framealpha": 1.0,
        "figure.figsize": (8, 6),
        "figure.titleweight": 600,
        "savefig.pad_inches": 0.2,
        "figure.titlesize": "larger",
    }
    return style_dict


def light_theme(
    palette: Optional[str] = None,
    context: Optional[str] = "notebook",
    grid: Optional[bool] = True,
    minimal: Optional[bool] = False,
) -> None:
    """Default light theme.

    Args:
        palette (Optional[str]): Colour palette to use.
        minimal (Optional[bool]): If yes will remove some line items such as
            grids, splines (borders), lengend frame edges.
        context (Optional[str], optional): Plots use context, this allows for
            adequate scaling of fonts and line elements. Can be one of "print",
            "notebook", "presentation". Defaults to "notebook".
        grid (Optional[bool], optional): Param to turn grids on (True) or
            off (False). Defaults to True.
    """

    theme_dict = compose_theme(
        style="light",
        theme_dict=_base_theme(),
        palette=palette,
        context=context,
        grid=grid,
    )

    theme_dict.update(_light_settings())

    # Add the minimal settings last to avoid overriding it with other settings
    if minimal:
        theme_dict.update(_minimal())

    set_theme(theme_dict)


def dark_theme(
    palette: Optional[str] = None,
    context: Optional[str] = "notebook",
    grid: Optional[bool] = True,
    minimal: Optional[bool] = False,
) -> None:
    """Default dark theme.

    Args:
        palette (Optional[str]): Colour palette to use.
        minimal (Optional[bool]): If yes will remove some line items such as
            grids, splines (borders), lengend frame edges.
        context (Optional[str], optional): Plots use context, this allows for
            adequate scaling of fonts and line elements. Can be one of "print",
            "notebook", "presentation". Defaults to "notebook".
        grid (Optional[bool], optional): Param to turn grids on (True) or
            off (False). Defaults to True.
    """

    theme_dict = compose_theme(
        style="dark",
        theme_dict=_base_theme(),
        palette=palette,
        context=context,
        grid=grid,
    )

    theme_dict.update(_dark_settings())
    # Add the minimal settings last to avoid overriding it with other settings
    if minimal:
        theme_dict.update(_minimal())
    set_theme(theme_dict)


def _light_settings():
    """Default light settings for the theme - mostly only changes chart elements,
    colour palettes are changed through the styler method.

    Returns:
        light_settings (dict): Dictionary containing the light theme settings.
    """
    bg_color = "white"
    fg_color = Base.grey[800]
    fg_color_darker = Base.grey[900]
    fg_color_lighter = Base.grey[700]
    grid_color = Base.grey[300]

    light_settings = {
        "patch.edgecolor": bg_color,
        "patch.force_edgecolor": True,
        "text.color": fg_color,
        "axes.titlecolor": fg_color_darker,
        "axes.edgecolor": fg_color,
        "axes.labelcolor": fg_color,
        "axes.facecolor": bg_color,
        "xtick.color": fg_color,
        "ytick.color": fg_color,
        "grid.color": grid_color,
        "legend.edgecolor": fg_color_lighter,
        "legend.labelcolor": fg_color,
        "legend.facecolor": "inherit",
        "figure.facecolor": bg_color,
        "hatch.color": Base.grey[50],
    }
    return light_settings


def _dark_settings():
    """Default light settings for the theme - mostly only changes chart elements,
    colour palettes are changed through the styler method.

    Returns:
        light_settings (dict): Dictionary containing the light theme settings.
    """
    bg_color = Base.grey[900]
    fg_color = Base.grey[100]
    fg_color_lighter = Base.grey[50]
    fg_color_darker = Base.grey[200]
    grid_color = Base.grey[700]

    light_settings = {
        "patch.edgecolor": bg_color,
        "patch.force_edgecolor": True,
        "text.color": fg_color,
        "axes.titlecolor": fg_color_lighter,
        "axes.edgecolor": fg_color,
        "axes.labelcolor": fg_color,
        "axes.facecolor": bg_color,
        "xtick.color": fg_color,
        "ytick.color": fg_color,
        "grid.color": grid_color,
        "legend.edgecolor": fg_color_darker,
        "legend.labelcolor": fg_color,
        "legend.facecolor": "inherit",
        "figure.facecolor": bg_color,
        "hatch.color": Base.grey[50],
    }
    return light_settings


def _minimal():
    """Minimal theme - it removes some line items such as grids, splines
    (borders), legend frame edges."""

    minimal = {
        "axes.grid": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.edgecolor": "none",
    }

    return minimal
