# Copyright 2024 Quansight Labs. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


class ColorPalettes:
    """Quansight colour palettes. These can be used for both
    categorical and sequential data.

    By default we only use a subset of the full colour monochrome colour
    palettes to ensure the plots have enough colour contrast for accessibility
    in light (900-500) and dark themes (400-50).

    - Monochrome: violet, plum, green
    -
    """

    violet = {
        900: "#E2D4FF",
        800: "#AF8AFF",
        700: "#9559FF",
        600: "#672BEC",
        500: "#4D1EB7",
        400: "#46209B",
        300: "#3F1E8A",
        200: "#2E1466",
        100: "#200E48",
        50: "#160048",
    }

    plum = {
        900: "#501A45",
        800: "#652058",
        700: "#7E286D",
        600: "#973083",
        500: "#B2399A",
        400: "#C05DAC",
        300: "#CE82BF",
        200: "#DEAAD4",
        100: "#EDCFE7",
        50: "#CE82BF",
    }

    green = {
        900: "#344515",
        800: "#42581A",
        700: "#526D21",
        600: "#638327",
        500: "#749A2E",
        400: "#8DAC54",
        300: "#A7BF7B",
        200: "#C3D4A5",
        100: "#DEE7CD",
        50: "#A7BF7B",
    }

    colorful_light = {
        "Purple": "#A543EF",
        "Magenta": "#9F1853",
        "Yellow": "#9C7110",
        "Blue": "#002D9C",
        "Teal": "#12847C",
        "Cyan": "#153167",
    }

    colorful_dark = {
        "Purple": "#C276FC",
        "Magenta": "#D12771",
        "Yellow": "#FEB000",
        "Blue": "#4589FF",
        "Teal": "#11AA9F",
        "Cyan": "#5073B7",
    }

    bright = {
        "Blue": "#648FFF",
        "Purple": "#785EF0",
        "Magenta": "#DC267F",
        "Orange": "#FE6100",
        "Golden": "#FFB000",
    }


class Diverging:
    """Diverging colour palettes."""

    plum_green = [
        "#30003A",
        "#611770",
        "#86599B",
        "#E1C9E2",
        "#D1EEC9",
        "#4BA24F",
        "#19672A",
        "#063615",
    ]
    purple_teal = [
        "#491D8B",
        "#6929C4",
        "#8A3FFC",
        "#A56EFF",
        "#BE95FF",
        "#D4BBFF",
        "#E8DAFF",
        "#F6F2FF",
        "#D9FBFB",
        "#9EF0F0",
        "#3DDBD9",
        "#08BDBA",
        "#009D9A",
        "#007D79",
        "#005D5D",
        "#004144",
    ]


class Base:
    """Class to hold the base colours - greys - to be used in the themes.
    These colurs are mainly used for backgrounds, axes, titles and the such.
    """

    grey = {
        900: "#25272C",
        800: "#3C4048",
        700: "#555B66",
        600: "#707785",
        500: "#8C929F",
        400: "#AAAEBB",
        300: "#C3C6CD",
        200: "#DDDEE2",
        100: "#EBECEE",
        50: "#F9F9FA",
    }
