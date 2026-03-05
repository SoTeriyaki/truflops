import math


def format_xy(x, y):
    return f"X{x:.3f} Y{y:.3f}"


def generate_circle(contour):

    cx, cy = contour["center"]
    r = contour["radius"]

    sx, sy = contour["start"]

    direction = contour["direction"]

    # punkt po przeciwnej stronie koła
    ex = cx - (sx - cx)
    ey = cy - (sy - cy)

    lines = []

    # szybki najazd
    lines.append(f"G00 X{sx:.3f} Y{sy:.3f}")

    # przebicie
    lines.append("TC_PIERCE")

    # wektory środka
    i1 = cx - sx
    j1 = cy - sy

    i2 = cx - ex
    j2 = cy - ey

    if direction == "CW":
        g = "G2"
    else:
        g = "G3"

    # pierwszy półokrąg
    lines.append(f"{g} X{ex:.3f} Y{ey:.3f} I{i1:.3f} J{j1:.3f}")

    # drugi półokrąg
    lines.append(f"{g} X{sx:.3f} Y{sy:.3f} I{i2:.3f} J{j2:.3f}")

    return lines

    # move to start
    lines.append(f"G00 {format_xy(sx, sy)}")

    # pierce
    lines.append("TC_PIERCE")

    # arc move
    i = cx - sx
    j = cy - sy

    if direction == "CW":
        g = "G2"
    else:
        g = "G3"

    lines.append(f"{g} I{i:.3f} J{j:.3f}")

    return lines


def generate_line(contour):

    x1, y1 = contour["start"]
    x2, y2 = contour["end"]

    lines = []

    lines.append(f"G00 {format_xy(x1, y1)}")
    lines.append("TC_PIERCE")
    lines.append(f"G01 {format_xy(x2, y2)}")

    return lines


def generate_arc(contour):

    sx, sy = contour["start"]
    ex, ey = contour["end"]

    cx, cy = contour["center"]

    direction = contour["direction"]

    i = cx - sx
    j = cy - sy

    if direction == "CW":
        g = "G2"
    else:
        g = "G3"

    lines = []

    lines.append(f"G00 {format_xy(sx, sy)}")
    lines.append("TC_PIERCE")
    lines.append(f"{g} {format_xy(ex, ey)} I{i:.3f} J{j:.3f}")

    return lines


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

    return "\n".join(lines)