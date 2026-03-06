import math
from post.pierce import generate_pierce_cycle


def format_xy(x, y):
    return f"X{x:.3f} Y{y:.3f}"


# =============================
# CIRCLE
# =============================

def generate_circle(contour):

    cx, cy = contour["center"]
    r = contour["radius"]

    sx, sy = contour["start"]
    lx, ly = contour["lead_start"]

    direction = contour["direction"]

    # punkt po przeciwnej stronie okręgu
    ex = cx - (sx - cx)
    ey = cy - (sy - cy)

    lines = []

    # szybki najazd na lead
    lines.append(f"G00 {format_xy(lx, ly)}")

    # pierce cycle
    lines += generate_pierce_cycle()

    # wejście na kontur
    lines.append(f"G01 {format_xy(sx, sy)}")

    # wektory środka
    i1 = cx - sx
    j1 = cy - sy

    i2 = cx - ex
    j2 = cy - ey

    g = "G2" if direction == "CW" else "G3"

    # pół okręgu
    lines.append(f"{g} {format_xy(ex, ey)} I{i1:.3f} J{j1:.3f}")

    # druga połowa
    lines.append(f"{g} {format_xy(sx, sy)} I{i2:.3f} J{j2:.3f}")

    return lines


# =============================
# LINE
# =============================

def generate_line(contour):

    x1, y1 = contour["start"]
    x2, y2 = contour["end"]

    lines = []

    lines.append(f"G00 {format_xy(x1, y1)}")
    lines += generate_pierce_cycle()
    lines.append(f"G01 {format_xy(x2, y2)}")

    return lines


# =============================
# ARC
# =============================

def generate_arc(contour):

    sx, sy = contour["start"]
    ex, ey = contour["end"]

    cx, cy = contour["center"]

    direction = contour["direction"]

    i = cx - sx
    j = cy - sy

    g = "G2" if direction == "CW" else "G3"

    lines = []

    lines.append(f"G00 {format_xy(sx, sy)}")
    lines += generate_pierce_cycle()

    lines.append(
        f"{g} {format_xy(ex, ey)} I{i:.3f} J{j:.3f}"
    )

    return lines


# =============================
# SUBPROGRAM
# =============================

def generate_subprogram(contours):

    lines = []

    for contour in contours:

        if contour["type"] == "circle":
            lines += generate_circle(contour)

        elif contour["type"] == "line":
            lines += generate_line(contour)

        elif contour["type"] == "arc":
            lines += generate_arc(contour)

        lines.append("")

def generate_dry_run_toolpath(contours):

    lines = []

    for contour in contours:

        if contour["type"] == "circle":

            sx, sy = contour["start"]
            ex, ey = contour["start"]   # wracamy do startu po pełnym okręgu
            cx, cy = contour["center"]
            direction = contour["direction"]

            g = "G2" if direction == "CW" else "G3"

            i = cx - sx
            j = cy - sy

            lines.append(f"G00 X{sx:.3f} Y{sy:.3f}")
            lines.append(f"{g} I{i:.3f} J{j:.3f}")

        elif contour["type"] == "line":

            x1, y1 = contour["start"]
            x2, y2 = contour["end"]

            lines.append(f"G00 X{x1:.3f} Y{y1:.3f}")
            lines.append(f"G01 X{x2:.3f} Y{y2:.3f}")

        elif contour["type"] == "arc":

            sx, sy = contour["start"]
            ex, ey = contour["end"]
            cx, cy = contour["center"]
            direction = contour["direction"]

            i = cx - sx
            j = cy - sy

            g = "G2" if direction == "CW" else "G3"

            lines.append(f"G00 X{sx:.3f} Y{sy:.3f}")
            lines.append(f"{g} X{ex:.3f} Y{ey:.3f} I{i:.3f} J{j:.3f}")

        lines.append("")

    return "\n".join(lines)