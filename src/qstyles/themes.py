from typing import Optional

from qstyles.palettes import Base
from qstyles.styler import create_palette, set_theme


def _base_theme() -> dict:
    style_dict = {
        "lines.linewidth": 1.5,
        "lines.markersize": 4.0,
        "hatch.linewidth": 2.0,
        "font.family": ["sans-serif"],
        "font.sans-serif": ["Arial", "DejaVu Sans", "sans-serif"],
        "font.size": 14.0,
        "axes.titlesize": "x-large",
        "axes.titlepad": 16.0,
        "axes.titleweight": "bold",
        "axes.labelsize": "medium",
        "axes.labelpad": 8.0,
        "axes.labelweight": 600,
        "axes.linewidth": 1.0,
        "axes.grid": True,
        "axes.grid.which": "major",
        "xtick.labelsize": "small",
        "ytick.labelsize": "small",
        "xtick.major.size": 8.25,
        "xtick.minor.size": 4.125,
        "xtick.major.width": 0.75,
        "xtick.minor.width": 0.75,
        "xtick.major.pad": 6,
        "xtick.minor.pad": 6,
        "xtick.direction": "out",
        "xtick.minor.visible": False,
        "ytick.major.size": 8.25,
        "ytick.minor.size": 4.125,
        "ytick.major.width": 0.75,
        "ytick.minor.width": 0.75,
        "ytick.major.pad": 6,
        "ytick.minor.pad": 6,
        "ytick.direction": "out",
        "ytick.minor.visible": False,
        "grid.linewidth": 0.75,
        "grid.alpha": 0.5,
        "legend.fontsize": "medium",
        "legend.title_fontsize": "medium",
        "legend.fancybox": True,
        "figure.figsize": (8, 6),
        "figure.titlesize": "larger",
        "figure.titleweight": "600",
    }
    return style_dict


def light_theme(palette: Optional[str] = None):
    # apply base theme first
    theme_dict = _base_theme()

    if palette:
        color_palette = create_palette(palette, "light")
    else:
        color_palette = create_palette("violet", "light")

    palette = {
        "axes.prop_cycle": color_palette,
    }
    theme_dict.update(palette)
    theme_dict.update(_light_settings())

    set_theme(theme_dict)


def dark_theme(palette: Optional[str] = None):
    # apply base theme first
    theme_dict = _base_theme()

    if palette:
        color_palette = create_palette(palette, "dark")
    else:
        color_palette = create_palette("violet", "dark")

    palette = {
        "axes.prop_cycle": color_palette,
    }
    theme_dict.update(palette)
    theme_dict.update(_dark_settings())

    set_theme(theme_dict)


def _light_settings():
    light_settings = {
        "patch.edgecolor": "w",
        "patch.force_edgecolor": True,
        "text.color": Base.grey[800],
        "axes.titlecolor": Base.grey[800],
        "axes.edgecolor": Base.grey[800],
        "axes.labelcolor": Base.grey[800],
        "axes.facecolor": "white",
        "xtick.color": Base.grey[800],
        "ytick.color": Base.grey[800],
        "grid.color": Base.grey[300],
        "legend.edgecolor": Base.grey[600],
        "legend.labelcolor": Base.grey[800],
        "legend.facecolor": "inherit",
        "legend.frameon": True,
        "legend.framealpha": 1.0,
        "figure.facecolor": "white",
        "hatch.color": Base.grey[50],
    }
    return light_settings


def _dark_settings():
    light_settings = {
        "patch.edgecolor": Base.grey[900],
        "patch.force_edgecolor": True,
        "text.color": Base.grey[100],
        "axes.titlecolor": Base.grey[50],
        "axes.edgecolor": Base.grey[300],
        "axes.labelcolor": Base.grey[100],
        "axes.facecolor": Base.grey[900],
        "xtick.color": Base.grey[300],
        "ytick.color": Base.grey[300],
        "grid.color": Base.grey[700],
        "legend.edgecolor": Base.grey[600],
        "legend.labelcolor": Base.grey[100],
        "legend.facecolor": "inherit",
        "legend.frameon": True,
        "legend.framealpha": 1.0,
        "figure.facecolor": Base.grey[900],
        "hatch.color": Base.grey[50],
    }
    return light_settings
