# Copyright 2024 Quansight Labs. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# Colours from the Quansight brand colour system:
# https://www.figma.com/design/bIeauLtP07MiUvDc24PNA4/PBC-Rebranding?node-id=336-2


class Sequential:
    """Monochrome colour palettes. These can be used for both
    categorical and sequential data.

    Each hue has 10 shades from 50 to 900, all on one shared lightness
    ladder, so the same stop has the same lightness in every hue.
    The light and dark palettes use a 5-stop subset of each ramp so that
    every colour has at least 3:1 contrast against the theme background
    (WCAG 1.4.11).
    """

    qs_violet = {
        900: "#10022F",
        800: "#29125C",
        700: "#452392",
        600: "#5D34BD",
        500: "#744DE0",
        400: "#8B6BF9",
        300: "#A390FF",
        200: "#BDB3FF",
        100: "#D8D4FF",
        50: "#F5F4FF",
    }
    qs_pink = {
        900: "#200116",
        800: "#440B33",
        700: "#6D1954",
        600: "#902770",
        500: "#AF3E8A",
        400: "#C95CA3",
        300: "#DD80BA",
        200: "#E9A7CE",
        100: "#F3CDE3",
        50: "#FFF1F9",
    }
    qs_teal = {
        900: "#001212",
        800: "#002D2E",
        700: "#004C4C",
        600: "#006667",
        500: "#008182",
        400: "#009D9F",
        300: "#38B8BA",
        200: "#83CECE",
        100: "#BCE3E2",
        50: "#E6FBFA",
    }
    psf_blue = {
        900: "#041E4F",
        800: "#1B3971",
        700: "#244C97",
        600: "#2D5FBD",
        500: "#4C7AD1",
        400: "#779DE5",
        300: "#90B0EB",
        200: "#ABC4F2",
        100: "#C7D9F8",
        50: "#E6EEFF",
    }

    # Dark and light palettes for each of the monochrome colour palettes.
    qs_violet_dark = [
        qs_violet[100],
        qs_violet[200],
        qs_violet[300],
        qs_violet[400],
        qs_violet[500],
    ]
    qs_violet_light = [
        qs_violet[400],
        qs_violet[500],
        qs_violet[600],
        qs_violet[700],
        qs_violet[800],
    ]
    qs_pink_dark = [
        qs_pink[100],
        qs_pink[200],
        qs_pink[300],
        qs_pink[400],
        qs_pink[500],
    ]
    qs_pink_light = [
        qs_pink[400],
        qs_pink[500],
        qs_pink[600],
        qs_pink[700],
        qs_pink[800],
    ]
    qs_teal_dark = [
        qs_teal[100],
        qs_teal[200],
        qs_teal[300],
        qs_teal[400],
        qs_teal[500],
    ]
    qs_teal_light = [
        qs_teal[400],
        qs_teal[500],
        qs_teal[600],
        qs_teal[700],
        qs_teal[800],
    ]
    psf_blue_dark = [
        psf_blue[50],
        psf_blue[100],
        psf_blue[200],
        psf_blue[300],
        psf_blue[400],
    ]
    psf_blue_light = [
        psf_blue[500],
        psf_blue[600],
        psf_blue[700],
        psf_blue[800],
        psf_blue[900],
    ]


class Categorical:
    """Categorical colour palettes, built from the brand hues (violet, teal,
    pink) plus three semantic hues (amber, green, red). Every pair stays
    distinguishable under protanopia, deuteranopia and tritanopia.
    """

    cat_qs_light = {
        "Violet": "#452392",
        "Teal": "#009D9F",
        "Pink": "#AF3E8A",
        "Amber": "#CB6E00",
        "Green": "#006B2C",
        "Red": "#D1131B",
    }
    cat_qs_dark = {
        "Violet": "#A390FF",
        "Teal": "#38B8BA",
        "Pink": "#C95CA3",
        "Amber": "#E08D48",
        "Green": "#91D09C",
        "Red": "#EC443C",
    }


class Diverging:
    """Diverging colour palettes: two brand hues meeting at a neutral
    midpoint, built from ramp stops 700, 500, 300 and 100.
    """

    qs_teal_pink = [
        "#004C4C",
        "#008182",
        "#38B8BA",
        "#BCE3E2",
        "#F6F6F5",
        "#F3CDE3",
        "#DD80BA",
        "#AF3E8A",
        "#6D1954",
    ]
    qs_pink_violet = [
        "#6D1954",
        "#AF3E8A",
        "#DD80BA",
        "#F3CDE3",
        "#F6F6F5",
        "#D8D4FF",
        "#A390FF",
        "#744DE0",
        "#452392",
    ]
    qs_violet_teal = [
        "#452392",
        "#744DE0",
        "#A390FF",
        "#D8D4FF",
        "#F6F6F5",
        "#BCE3E2",
        "#38B8BA",
        "#008182",
        "#004C4C",
    ]


class Base:
    """Class to hold the base colours - greys - to be used in the themes.
    These colours are mainly used for base chart elements, such as backgrounds,
    axes, titles and other common plot elements.
    """

    grey = {
        900: "#0F0E0D",
        800: "#282625",
        700: "#43413F",
        600: "#5A5856",
        500: "#73706E",
        400: "#8C8987",
        300: "#A5A3A1",
        200: "#BFBEBC",
        100: "#DAD9D9",
        50: "#F6F6F5",
    }

    grey_dark = [
        grey[100],
        grey[200],
        grey[300],
        grey[400],
        grey[500],
    ]
    grey_light = [
        grey[400],
        grey[500],
        grey[600],
        grey[700],
        grey[800],
    ]
