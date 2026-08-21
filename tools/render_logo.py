"""Render the Aetheris logo.svg to PNG files.

Discord's embed image proxy refuses SVG payloads, so we rasterize the
official logo into:
  - assets/logo.png  (full wordmark lockup)
  - assets/icon.png  (square icon-only mark, used as embed footer icon)

Pure Pillow implementation - no external SVG renderer required.
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

# --- Colors -------------------------------------------------------------
C_EMERALD_START = (16, 185, 129)  # #10B981
C_EMERALD_END = (5, 150, 105)     # #059669
C_ICON_TOP = (52, 211, 153)       # #34D399
C_ICON_MID = (16, 185, 129)       # #10B981
C_ICON_END = (5, 150, 105)        # #059669
C_WORD = (250, 250, 250)          # #FAFAFA
C_TAG = (113, 113, 122)           # #71717A
C_GLOW = (16, 185, 129, 130)

# viewBox geometry (same as logo.svg)
OUTER = [(40, 5), (70, 22), (70, 58), (40, 75), (10, 58), (10, 22)]
INNER = [(40, 20), (55, 30), (55, 50), (40, 60), (25, 50), (25, 30)]
A_PATH = [(40, 25), (55, 55), (50, 55), (47, 48), (33, 48), (30, 55), (25, 55)]
A_CUT = [(35, 44), (45, 44), (40, 32)]
DOTS = [(40, 12, 4, 1.0), (15, 28, 3, 0.7), (65, 28, 3, 0.7),
        (15, 52, 3, 0.7), (65, 52, 3, 0.7), (40, 68, 4, 1.0)]


def lerp(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def diagonal_gradient(size, stops):
    """Two-point diagonal gradient across the given size."""
    w, h = size
    img = Image.new("RGB", size)
    px = img.load()
    for y in range(h):
        for x in range(w):
            t = (x / max(w - 1, 1) + y / max(h - 1, 1)) / 2
            t = max(0.0, min(1.0, t))
            if len(stops) == 2:
                color = lerp(stops[0], stops[1], t)
            else:
                if t < 0.5:
                    color = lerp(stops[0], stops[1], t * 2)
                else:
                    color = lerp(stops[1], stops[2], (t - 0.5) * 2)
            px[x, y] = color
    return img


def pick_font(size, bold=True):
    candidates = (
        ["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
        if bold
        else ["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    )
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def icon_layer(size=80):
    """Draw the hexagon 'A' mark at native 80x80 (viewBox coords)."""
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)

    icon_grad = diagonal_gradient((80, 80), [C_ICON_TOP, C_ICON_MID, C_ICON_END])
    emerald_grad = diagonal_gradient((60, 60), [C_EMERALD_START, C_EMERALD_END])

    # Glow
    glow = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r in (6, 4, 2):
        gd.line(OUTER + [OUTER[0]], fill=C_GLOW, width=r)
    layer.paste(glow, (0, 0), glow)

    # Inner hexagon (15% opacity gradient fill)
    inner_img = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
    inner_img.paste(icon_grad, (0, 0))
    idraw = ImageDraw.Draw(inner_img)
    idraw.polygon(INNER, fill=(255, 255, 255, 38))
    layer.paste(inner_img, (0, 0), inner_img)

    # Outer hexagon stroke (emerald gradient -> light to dark)
    d.line(OUTER + [OUTER[0]], fill=C_EMERALD_START, width=3)

    # "A" letterform filled with gradient
    a_img = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
    a_img.paste(emerald_grad, (0, 0))
    adraw = ImageDraw.Draw(a_img)
    adraw.polygon(A_PATH, fill=(255, 255, 255, 255))
    cut = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
    cdraw = ImageDraw.Draw(cut)
    cdraw.polygon(A_CUT, fill=(0, 0, 0, 255))
    a_img.paste(cut, (0, 0), cut)
    layer.paste(a_img, (0, 0), a_img)

    # Node dots
    for dx, dy, r, op in DOTS:
        dot = Image.new("RGBA", (80, 80), (0, 0, 0, 0))
        ddraw = ImageDraw.Draw(dot)
        ddraw.ellipse((dx - r, dy - r, dx + r, dy + r),
                      fill=(16, 185, 129, round(255 * op)))
        layer.paste(dot, (0, 0), dot)

    return layer


def render_full():
    """400x100 lockup at 2x scale."""
    S = 2
    img = Image.new("RGBA", (400 * S, 100 * S), (0, 0, 0, 0))

    icon = icon_layer(80).resize((80 * S, 80 * S), Image.LANCZOS)
    img.paste(icon, (10 * S, 10 * S), icon)

    d = ImageDraw.Draw(img)
    word_font = pick_font(48 * S, bold=True)
    d.text((95 * S, 62 * S - 48 * S), "Aetheris", font=word_font, fill=C_WORD)

    tag_font = pick_font(12 * S, bold=False)
    d.text((95 * S, 82 * S - 12 * S), "ENTERPRISE PLATFORM",
           font=tag_font, fill=C_TAG)

    return img


def render_icon():
    """512x512 square icon for embed footers."""
    return icon_layer(80).resize((512, 512), Image.LANCZOS)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    full = render_full()
    full.save(ASSETS / "logo.png", "PNG")
    icon = render_icon()
    icon.save(ASSETS / "icon.png", "PNG")
    print(f"Wrote {ASSETS / 'logo.png'} ({full.size})")
    print(f"Wrote {ASSETS / 'icon.png'} ({icon.size})")


if __name__ == "__main__":
    main()
