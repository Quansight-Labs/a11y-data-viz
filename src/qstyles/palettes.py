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
        900: "#1F0547",
        800: "#2A0A63",
        700: "#37127F",
        600: "#46209B",
        500: "#5C35B0",
        400: "#8767CE",
        300: "#9D80DB",
        200: "#AD93E4",
        100: "#C1ADED",
        50: "#D7C8F6",
    }
    plum = {
        900: "#541140",
        800: "#6B1755",
        700: "#831F6A",
        600: "#9A2A81",
        500: "#B2399A",
        400: "#C658B2",
        300: "#D97FCB",
        200: "#E399D6",
        100: "#ECB5E2",
        50: "#F6D3EF",
    }
    green = {
        900: "#263513",
        800: "#394E1A",
        700: "#4B6820",
        600: "#5F8126",
        500: "#749A2E",
        400: "#8DB34B",
        300: "#A9CC70",
        200: "#BAD98C",
        100: "#CDE6AB",
        50: "#E2F2CC",
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
    teal = {
        900: "#042A22",
        800: "#08483B",
        700: "#0E6655",
        600: "#18846F",
        500: "#28A188",
        400: "#40BFA2",
        300: "#80E1BC",
        200: "#9BEBC7",
        100: "#B9F5D6",
        50: "#D9FFE9",
    }

    violet_dark = [
        violet[50],
        violet[100],
        violet[200],
        violet[300],
        violet[400],
    ]
    violet_light = [
        violet[300],
        violet[400],
        violet[500],
        violet[700],
        violet[900],
    ]

    green_dark = [
        green[50],
        green[100],
        green[200],
        green[300],
        green[400],
    ]
    green_light = [
        green[500],
        green[600],
        green[700],
        green[800],
        green[900],
    ]

    plum_dark = [
        plum[50],
        plum[100],
        plum[200],
        plum[300],
        plum[400],
    ]
    plum_light = [
        plum[400],
        plum[500],
        plum[600],
        plum[700],
        plum[800],
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

    teal_dark = [
        teal[50],
        teal[100],
        teal[200],
        teal[300],
        teal[400],
    ]
    teal_light = [
        teal[500],
        teal[600],
        teal[700],
        teal[800],
        teal[900],
    ]


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
        "#541140",
        "#831F6A",
        "#B2399A",
        "#C658B2",
        "#D97FCB",
        "#ECB5E2",
        "#F6D3EF",
        "#F8F4F2",
        "#E2F2CC",
        "#CDE6AB",
        "#A9CC70",
        "#8DB34B",
        "#749A2E",
        "#4B6820",
        "#263513",
    ]
    green_violet = [
        "#263513",
        "#4B6820",
        "#749A2E",
        "#8DB34B",
        "#A9CC70",
        "#CDE6AB",
        "#E2F2CC",
        "#F4F5F5",
        "#D7C8F6",
        "#C1ADED",
        "#9D80DB",
        "#8767CE",
        "#5C35B0",
        "#37127F",
        "#1F0547",
    ]


class Base:
    """Class to hold the base colours - greys - to be used in the themes.
    These colours are mainly used for backgrounds, axes, titles and the such.
    """

    grey = {
        900: "#25272C",
        800: "#3C4048",
        700: "#555B66",
        600: "#707785",
        500: "#8A909E",
        400: "#AAAEBB",
        300: "#C3C6CD",
        200: "#DDDEE2",
        100: "#EBECEE",
        50: "#F9F9FA",
    }

    grey_dark = [
        grey[50],
        grey[100],
        grey[200],
        grey[300],
        grey[400],
    ]
    grey_light = [
        grey[500],
        grey[600],
        grey[700],
        grey[800],
        grey[400],
    ]
