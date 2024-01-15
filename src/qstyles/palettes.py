# Copyright 2024 Quansight Labs. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


class Sequential:
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

    purple = {
        900: "#312a7d",
        800: "#5238a7",
        700: "#764bc5",
        600: "#976acd",
        500: "#b48ad1",
        400: "#cdabd7",
        300: "#e1cde1",
    }

    purple_dark = [
        purple[300],
        purple[400],
        purple[500],
        purple[600],
        purple[700],
    ]
    purple_light = [
        purple[900],
        purple[800],
        purple[700],
        purple[600],
        purple[500],
    ]

    teal = {
        900: "#0c5d64",
        800: "#127577",
        700: "#198d87",
        600: "#20a796",
        500: "#40bfa2",
        400: "#7cd2b0",
        300: "#b9e0c9",
    }

    teal_dark = [teal[300], teal[400], teal[500], teal[600], teal[700]]
    teal_light = [teal[900], teal[800], teal[700], teal[600], teal[500]]


class Categorical:
    cat_colorful_light = {
        "Blue": "#002D9C",
        "Purple": "#A543EF",
        "Yellow": "#9C7110",
        "Magenta": "#9F1853",
        "Teal": "#12847C",
        "Cyan": "#153167",
    }

    cat_colorful_dark = {
        "Blue": "#8aabfd",
        "Purple": "#a07bde",
        "Yellow": "#e3b13e",
        "Magenta": "#ae49a2",
        "Teal": "#4fbbae",
        "Cyan": "#5073B7",
    }

    cat_bright = {
        "Blue": "#648FFF",
        "Purple": "#785EF0",
        "Magenta": "#DC267F",
        "Orange": "#FE6100",
        "Golden": "#FFB000",
    }

    cat_qs_dark = {
        "Teal": "#4C9AAF",
        "Blue": "#4B92E5",
        "Indigo": "#997AFC",
        "Purple": "#C89EF1",
        "Magenta": "#DA62C6",
        "Orange": "#DF8855",
        "Yellow": "#FAE275",
    }

    cat_qs_light = {
        "Teal": "#4C9AAF",
        "Blue": "#4B92E5",
        "Indigo": "#997AFC",
        "Purple": "#B176E2",
        "Magenta": "#DA62C4",
        "Orange": "#CA704A",
        "Yellow": "#97933E",
    }


class Diverging:
    """Diverging colour palettes."""

    plum_green = [
        "#7c2d73",
        "#983b8d",
        "#b34ea6",
        "#c769ba",
        "#d588c9",
        "#dfa9d6",
        "#eac9e4",
        "#9fe4db",
        "#6fd2c5",
        "#4cbcaf",
        "#32a599",
        "#1e8d83",
        "#08766d",
        "#005f57",
    ]
    teal_purple = [
        "#09443a",
        "#105f52",
        "#187b6b",
        "#1e9884",
        "#29b69f",
        "#5cd0ba",
        "#a0e5d5",
        "#d5cff1",
        "#bbafea",
        "#a28ee3",
        "#8a6cda",
        "#734cc8",
        "#5a34a4",
        "#402379",
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
