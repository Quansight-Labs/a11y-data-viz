import matplotlib as mpl

from cycler import cycler

from qstyles.palettes import ColorPalettes, Diverging


def create_palette(palette: str, scheme: str) -> cycler:
    """Helper function to build a repeating list of colors for matplotlib

    Args:
        hex_values (list): A list of hex values for colors to use as a color palette

    Returns:
        cycler: A cycler object that can be used to set the color palette for matplotlib
    """

    diverging_palettes = ["plum_green", "purple_teal"]
    categorical_palettes = ["colorful_light", "colorful_dark", "bright"]
    mono_palettes = ["violet", "green", "plum"]

    if palette in diverging_palettes:
        hex_values = getattr(Diverging, palette)

    elif palette in categorical_palettes:
        hex_values = list(getattr(ColorPalettes, palette).values())

    elif palette in mono_palettes:
        hex_values = list(getattr(ColorPalettes, palette).values())
        if scheme == "dark":
            hex_values = hex_values[:5]
        else:
            hex_values = hex_values[5:][::-1]

    return cycler("color", hex_values)


def set_theme(theme_params: dict) -> None:
    """Pass a dict of style params to matplotlib

    Args:
        theme_params (dict): style params used to override matplotlib.rcParams
    """
    mpl.rcParams.update(theme_params)
