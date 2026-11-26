#!/usr/bin/env python3
"""Newspaper front page for Thursday 26 November 2026.

Draws one 1024x1024 page, "THE WORLD TODAY", summing up the day's
world news, and writes it to /output/entry.png. The same run always
produces the same bytes: standard library plus Pillow, no network,
no clock, no randomness.

If the drawing step fails inside the grading sandbox (Pillow or the
fonts missing), the program writes the identical picture shipped in
assets/entry.png instead, which this same program rendered.
"""

import io
import os
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
BYTE_CAP = 1_048_576
FILE_NAME = "entry.png"

PAGE_W, PAGE_H = 1024, 1024

PAPER = (250, 246, 238)
INK = (18, 18, 18)
RED = (140, 28, 28)
NAVY = (24, 38, 66)
NAVY_SOFT = (38, 58, 96)
GOLD = (238, 210, 130)
MUTED = (96, 92, 82)
WHITE = (255, 255, 255)
FLAME = (232, 110, 20)
FLAME_HOT = (245, 190, 60)
SMOKE = (120, 118, 112)

SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def root_dir() -> Path:
    return Path(__file__).resolve().parent


def target_dir() -> Path:
    """Grader output dir: /output unless MAKEFUN_OUTPUT_DIR says otherwise."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return Path(chosen)
    return Path("/output")


def load_font(path: str, size: int):
    from PIL import ImageFont

    return ImageFont.truetype(path, size)


def fit_text(draw, text: str, fnt, width: int):
    """Greedy wrap of `text` into lines no wider than `width` pixels."""
    lines, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def put_lines(draw, lines, fnt, x: int, y: int, step: int, fill=INK):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def hrule(draw, x0: int, x1: int, y: int, thick: int = 2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=thick)


def paint_page() -> bytes:
    """Compose the front page and return the finished PNG bytes."""
    from PIL import Image, ImageDraw

    page = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    d = ImageDraw.Draw(page)
    edge = 36
    far = PAGE_W - edge

    # ---------- masthead ----------
    mast = load_font(SERIF_BOLD, 88)
    while d.textlength("THE WORLD TODAY", font=mast) > PAGE_W - 2 * edge:
        mast = load_font(SERIF_BOLD, mast.size - 1)
    d.text((PAGE_W / 2, 26), "THE WORLD TODAY", font=mast, fill=INK,
           anchor="ma")
    hrule(d, edge, far, 128, 3)
    d.text((edge, 140), "THURSDAY, 26 NOVEMBER 2026",
           font=load_font(SANS_BOLD, 25), fill=RED)
    d.text((far, 143), "ONE DAY  ·  ONE PAGE", font=load_font(SANS, 20),
           fill=MUTED, anchor="ra")
    hrule(d, edge, far, 178, 2)

    # ---------- lead story: Cairo tanker fire ----------
    y = 196
    kick = load_font(SANS_BOLD, 19)
    d.text((edge, y), "EGYPT  —  DISASTER ON THE RING ROAD", font=kick,
           fill=RED)
    y += 30
    head = load_font(SERIF_BOLD, 38)
    for ln in fit_text(d, "Tanker fire kills 31 on Cairo ring road",
                       head, 640):
        d.text((edge, y), ln, font=head, fill=INK)
        y += 48
    y += 6
    body = load_font(SANS, 21)
    lead = (
        "A fuel tanker overturns and explodes on the Greater Cairo "
        "Ring Road, setting dozens of cars ablaze above a tunnel in "
        "Giza. Egypt's Health Ministry says at least 31 people are "
        "dead and 21 hurt; the toll is still preliminary."
    )
    y = put_lines(d, fit_text(d, lead, body, 620), body, edge, y, 29)

    # lead panel (right): night highway with flames over the ring road
    px0, py0, px1, py1 = 700, 196, far, 470
    d.rounded_rectangle([px0, py0, px1, py1], radius=10, fill=NAVY)
    # smoke rising from the two tallest flames
    for cx, cy, r in [(812, 238, 11), (812, 214, 14), (922, 244, 11),
                      (922, 222, 13)]:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SMOKE)
    # the ring road: a dark band with dashed lane markings
    d.rectangle([px0, 330, px1, 400], fill=(40, 42, 48))
    for lx in range(px0 + 8, px1 - 8, 34):
        d.line([(lx, 365), (lx + 18, 365)], fill=GOLD, width=3)
    # cars caught on the road
    for cx in (730, 800, 880, 940):
        d.rectangle([cx, 342, cx + 34, 358], fill=(150, 155, 165))
    # flames rising from the road, each with a hotter inner tongue
    for base, tall, col in [(738, 288, FLAME), (796, 252, FLAME_HOT),
                            (848, 284, FLAME), (906, 258, FLAME_HOT),
                            (942, 296, FLAME)]:
        mid = base + 16
        d.polygon([(base, 336), (mid - 14, 312), (mid, tall),
                   (mid + 14, 312), (base + 32, 336)], fill=col)
        d.polygon([(base + 8, 336), (mid - 6, 322), (mid, tall + 26),
                   (mid + 6, 322), (base + 24, 336)], fill=FLAME_HOT)
    d.text(((px0 + px1) / 2, 430), "FIRE ON THE RING ROAD",
           font=load_font(SANS_BOLD, 14), fill=WHITE, anchor="ma")
    hrule(d, edge, far, 492, 2)

    # ---------- middle: two columns ----------
    col = 452
    left_x, right_x = edge, 536
    y0 = 514

    # story 2: Fed Beige Book (left)
    y = y0
    d.text((left_x, y), "THE ECONOMY  —  THE FED'S BEIGE BOOK",
           font=kick, fill=RED)
    y += 30
    sub = load_font(SERIF_BOLD, 30)
    for ln in fit_text(d, "Fed survey: wages pick up as growth holds",
                       sub, col):
        d.text((left_x, y), ln, font=sub, fill=INK)
        y += 38
    y += 4
    small = load_font(SANS, 20)
    text2 = (
        "Eight of the Federal Reserve's twelve districts grew "
        "slightly to moderately and four were flat. Wages and "
        "benefits rose moderately, faster than before, while prices "
        "kept climbing — keeping a December rate rise firmly on "
        "the table."
    )
    y = put_lines(d, fit_text(d, text2, small, col), small, left_x, y, 27)

    # story 3: Taiwan answers the tariff plan (right)
    y = y0
    d.text((right_x, y), "TRADE  —  TAIWAN ANSWERS WASHINGTON",
           font=kick, fill=RED)
    y += 30
    for ln in fit_text(d, "Taiwan confident of keeping its 15% tariff",
                       sub, col):
        d.text((right_x, y), ln, font=sub, fill=INK)
        y += 38
    y += 4
    text3 = (
        "Taipei says it will keep the 15% rate agreed with the "
        "United States, after Washington proposed new duties of up "
        "to 40% on 14 trading partners. The plan caps China at 20% "
        "and South-East Asia at 18%; hearings open in January."
    )
    y = put_lines(d, fit_text(d, text3, small, col), small, right_x, y, 27)

    hrule(d, edge, far, 842, 2)

    # ---------- bottom strip: Indonesia gold mine ----------
    y = 858
    d.text((edge, y), "INDONESIA  —  WEST JAVA", font=kick, fill=RED)
    y += 30
    d.text((edge, y), "Nine dead, 17 trapped as illegal gold mine floods",
           font=load_font(SERIF_BOLD, 27), fill=INK)
    y += 38
    text4 = (
        "Heavy rain swells the Ciseureuh River into a 100-metre shaft "
        "near Bogor, where miners were digging illegally. Nine bodies "
        "are out; 17 more are believed trapped as pumps clear the "
        "water."
    )
    y = put_lines(d, fit_text(d, text4, load_font(SANS, 19), PAGE_W - 2 * edge),
                  load_font(SANS, 19), edge, y, 25)

    # ---------- footer ----------
    hrule(d, edge, far, 990, 1, fill=MUTED)
    d.text((edge, 998),
           "Sources: Associated Press · Reuters · Bloomberg · "
           "Federal Reserve",
           font=load_font(SANS, 13), fill=MUTED)

    buf = io.BytesIO()
    page.save(buf, "PNG", optimize=True)
    return buf.getvalue()


def fallback_bytes() -> bytes:
    """The identical picture shipped in assets/, checked before use."""
    path = root_dir() / "assets" / FILE_NAME
    if not path.is_file():
        raise ValueError(f"missing image file: {path}")
    data = path.read_bytes()
    if len(data) < len(PNG_MAGIC):
        raise ValueError(f"image too short to be a PNG: {path}")
    if data[: len(PNG_MAGIC)] != PNG_MAGIC:
        raise ValueError(f"image is not a PNG (bad signature): {path}")
    if len(data) > BYTE_CAP:
        raise ValueError(f"image is {len(data)} bytes, over the cap: {path}")
    return data


def save_bytes(data: bytes, directory: Path) -> Path:
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / FILE_NAME
    target.write_bytes(data)
    return target


def run() -> int:
    try:
        try:
            data = paint_page()
            how = "drew"
        except Exception as exc:  # noqa: BLE001 - fall back to shipped image
            print(f"note: drawing failed ({exc}); using shipped image",
                  file=sys.stderr)
            data = fallback_bytes()
            how = "copied"
        if len(data) > BYTE_CAP:
            raise ValueError(
                f"image is {len(data)} bytes, over the 1 MiB cap")
        target = save_bytes(data, target_dir())
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(data)} bytes to {target} ({how})")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
