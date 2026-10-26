import warnings

import pytest

from qstyles import dark_theme, light_theme, palettes
from qstyles.styler import PALETTES, create_palette


LIGHT_BG = "#FFFFFF"
DARK_BG = palettes.Base.grey[900]


def _luminance(hex_color):
    channels = [int(hex_color[i : i + 2], 16) / 255 for i in (1, 3, 5)]
    r, g, b = (
        c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
        for c in channels
    )
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _contrast(a, b):
    high, low = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def _colors(name):
    return create_palette(name).by_key()["color"]


@pytest.mark.parametrize("name", PALETTES)
def test_palette_resolves(name):
    assert len(_colors(name)) >= 5


@pytest.mark.parametrize(
    "name", [p for p in PALETTES if p.endswith(("_light", "_dark"))]
)
def test_palette_contrast(name):
    """Every mark colour has 3:1 against its theme background (WCAG 1.4.11)."""
    bg = DARK_BG if name.endswith("_dark") else LIGHT_BG
    for color in _colors(name):
        assert _contrast(color, bg) >= 3, f"{name} {color}"


def test_unknown_palette_errors():
    with pytest.raises(ValueError, match="Unknown palette"):
        create_palette("not_a_palette")


@pytest.mark.parametrize("theme", [light_theme, dark_theme])
def test_themes_apply(theme):
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        theme()
