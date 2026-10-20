import warnings

import pytest

from qstyles import dark_theme, light_theme
from qstyles.styler import PALETTES, create_palette


def _colors(name):
    return create_palette(name).by_key()["color"]


@pytest.mark.parametrize("name", PALETTES)
def test_palette_resolves(name):
    assert len(_colors(name)) >= 5


def test_unknown_palette_errors():
    with pytest.raises(ValueError, match="Unknown palette"):
        create_palette("not_a_palette")


@pytest.mark.parametrize("theme", [light_theme, dark_theme])
def test_themes_apply(theme):
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        theme()
