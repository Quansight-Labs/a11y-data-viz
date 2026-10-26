# Copyright 2024 Quansight Labs. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Render the example images in examples/images/.

Run from the repository root after changing a palette or theme:

    python scripts/render_examples.py

Every palette gets a folder. Palettes ending in _light or _dark are rendered
with the matching theme as bar, grid, lines and scatter plots. Diverging
palettes are rendered as a heatmap with the light theme only, since they
are designed for light backgrounds. A swatch overview of all
palettes is written to examples/images/palettes.png.
"""

import shutil

from pathlib import Path

import matplotlib as mpl


mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import LinearSegmentedColormap

import qstyles

from qstyles import palettes
from qstyles.styler import (
    BASE_PALETTES,
    CATEGORICAL_PALETTES,
    DIVERGING_PALETTES,
    SEQUENTIAL_PALETTES,
)


OUT = Path(__file__).resolve().parent.parent / "examples" / "images"
DPI = 100
# Every bar, line and scatter example draws six series, as the original
# images did, so 5-colour palettes show the colour cycle wrapping around.
SERIES = 6


def apply_theme(style, palette=None):
    mpl.rcdefaults()
    theme = qstyles.light_theme if style == "light" else qstyles.dark_theme
    theme(palette=palette)


def bar_plot(n):
    fig, ax = plt.subplots()
    x = np.arange(9)
    for i in range(n):
        heights = 6 - np.abs(x - 4) * 1.2 + (i % 3) * 0.3
        ax.bar(x + i * 5, heights, width=1, label=chr(65 + i))
    ax.set_title("Bar Plot")
    ax.legend()
    return fig


def lines_plot(n):
    fig, ax = plt.subplots()
    v = np.linspace(0.75, 1.25, 400)
    orders = [10, 15, 20, 30, 50, 100][:n]
    for order in orders:
        ax.plot(v, v**order / (1 + v**order) * (1 + 0.5 * (v - 1)))
    ax.set_xlim(0.75, 1.25)
    ax.set_ylim(0, 1.25)
    ax.set_xlabel("Voltage (mV)")
    ax.set_ylabel(r"Current ($\mu$A)")
    ax.set_title("Line Plot")
    ax.legend([str(o) for o in orders], title="Order")
    return fig


def scatter_plot(n, rng):
    fig, ax = plt.subplots()
    for i in range(n):
        x = rng.uniform(0, 1, 80)
        y = rng.uniform(0, 1, 80) + i
        ax.scatter(x, y, s=16, label=chr(65 + i))
    ax.set_title("Scatter Plot")
    ax.legend(loc="center left")
    return fig


def grid_plot(rng):
    fig = plt.figure(figsize=(15, 10))
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    ax = fig.add_subplot(2, 2, 1)
    t = np.linspace(0, 10, 500)
    for _ in range(4):
        ax.plot(t, np.cumsum(rng.normal(0, 1, t.size)))
    ax.set_xlim(0, 10)
    ax.set_xlabel("Time")
    ax.set_ylabel("Random values")
    ax.set_title("Line Plot")

    ax = fig.add_subplot(2, 2, 2)
    x = rng.uniform(-1, 3.4, 300)
    ax.scatter(
        x,
        np.sin(2.5 * x) * 0.6 + rng.normal(0, 0.2, x.size),
        marker="^",
        s=60,
        alpha=0.6,
        color=colors[1],
    )
    x = rng.uniform(0.6, 2.6, 150)
    ax.scatter(
        x,
        1.4 - 1.2 * (x - 1.6) ** 2 + rng.normal(0, 0.25, x.size),
        s=60,
        alpha=0.6,
        color=colors[2],
    )
    ax.set_xlabel("Space")
    ax.set_ylabel("Altitude")
    ax.set_title("Scatter Plot")

    ax = fig.add_subplot(2, 2, 3)
    data = np.concatenate([rng.normal(191, 6, 190), rng.normal(215, 7, 150)])
    ax.hist(data, bins=12, alpha=0.4, color=colors[0])
    grid = np.linspace(160, 245, 300)
    bw = 4.5
    kde = np.exp(-0.5 * ((grid[:, None] - data) / bw) ** 2).sum(axis=1)
    kde *= (data.max() - data.min()) / 12 / (bw * np.sqrt(2 * np.pi))
    ax.plot(grid, kde, color=colors[0])
    ax.set_xlabel("Flipper length (mm)")
    ax.set_ylabel("Density")
    ax.set_title("Distribution Plot")

    ax = fig.add_subplot(2, 2, 4, projection="polar")
    r = np.linspace(0, 3, 300)
    ax.plot(2 * np.pi * r, r)
    ax.plot(2 * np.pi * r * 0.8, r, linestyle="--")
    ax.set_title("Polar Axis Plot")
    return fig


def heatmap_plot(colors, rng):
    fig, ax = plt.subplots()
    cmap = LinearSegmentedColormap.from_list("diverging", colors)
    x, y = np.meshgrid(np.linspace(-3, 3, 40), np.linspace(-2, 2, 30))
    z = np.sin(x) * np.cos(y) + rng.normal(0, 0.05, x.shape)
    image = ax.imshow(z, cmap=cmap, vmin=-1, vmax=1, aspect="auto")
    ax.grid(False)
    fig.colorbar(image, ax=ax)
    ax.set_title("Heatmap")
    return fig


def save(fig, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=DPI)
    plt.close(fig)


def render_palette(name):
    style = "dark" if name.endswith("_dark") else "light"
    apply_theme(style, name)
    folder = OUT / name
    save(bar_plot(SERIES), folder / "bar.png")
    save(lines_plot(SERIES), folder / "lines.png")
    save(
        scatter_plot(SERIES, np.random.default_rng(1)), folder / "scatter.png"
    )
    save(grid_plot(np.random.default_rng(2)), folder / "grid.png")


def render_diverging(name):
    apply_theme("light")
    fig = heatmap_plot(
        getattr(palettes.Diverging, name), np.random.default_rng(3)
    )
    save(fig, OUT / name / "heatmap.png")


def palette_overview():
    apply_theme("light")
    rows = []
    for name in SEQUENTIAL_PALETTES:
        rows.append((name, getattr(palettes.Sequential, name)))
    for name in CATEGORICAL_PALETTES:
        rows.append((name, list(getattr(palettes.Categorical, name).values())))
    for name in DIVERGING_PALETTES:
        rows.append((name, getattr(palettes.Diverging, name)))
    for name in BASE_PALETTES:
        rows.append((name, getattr(palettes.Base, name)))

    fig, ax = plt.subplots(figsize=(10, 0.5 * len(rows) + 0.5))
    for row, (name, colors) in enumerate(rows):
        dark = name.endswith("_dark")
        ax.add_patch(
            plt.Rectangle(
                (-0.1, row - 0.45),
                9.2,
                0.9,
                color=palettes.Base.grey[900] if dark else "white",
                zorder=0,
            )
        )
        for col, color in enumerate(colors):
            ax.add_patch(
                plt.Rectangle(
                    (col, row - 0.35), 0.9, 0.7, color=color, linewidth=0
                )
            )
    ax.set_xlim(-0.1, 9.1)
    ax.set_ylim(len(rows) - 0.5, -0.5)
    ax.set_yticks(range(len(rows)), [name for name, _ in rows])
    ax.set_xticks([])
    ax.grid(False)
    for side in ("top", "right", "bottom", "left"):
        ax.spines[side].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_title("qstyles palettes")
    save(fig, OUT / "palettes.png")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    for name in SEQUENTIAL_PALETTES + CATEGORICAL_PALETTES + BASE_PALETTES:
        render_palette(name)
    for name in DIVERGING_PALETTES:
        render_diverging(name)
    palette_overview()
    count = len(list(OUT.rglob("*.png")))
    print(f"Wrote {count} images to {OUT}")  # noqa: T201


if __name__ == "__main__":
    main()
