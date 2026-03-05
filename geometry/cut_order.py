import math


def contour_size(contour):
    """
    Oblicza rozmiar konturu do sortowania
    """

    if contour["type"] == "circle":
        return contour["radius"]

    if contour["type"] == "arc":
        return contour["radius"]

    if contour["type"] == "line":
        x1, y1 = contour["start"]
        x2, y2 = contour["end"]
        return math.hypot(x2 - x1, y2 - y1)

    if contour["type"] == "polyline":
        return len(contour["points"])

    return 0


def contour_center(contour):
    """
    Przybliżony środek konturu
    """

    if contour["type"] == "circle":
        return contour["center"]

    if contour["type"] == "arc":
        return contour["center"]

    if contour["type"] == "line":
        x1, y1 = contour["start"]
        x2, y2 = contour["end"]
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    if contour["type"] == "polyline":
        xs = [p[0] for p in contour["points"]]
        ys = [p[1] for p in contour["points"]]
        return (sum(xs) / len(xs), sum(ys) / len(ys))

    return (0, 0)


def compute_bbox(contours):
    """
    Bounding box wszystkich konturów
    """

    xs = []
    ys = []

    for c in contours:

        if c["type"] == "circle":
            cx, cy = c["center"]
            r = c["radius"]

            xs += [cx - r, cx + r]
            ys += [cy - r, cy + r]

        elif c["type"] == "line":
            x1, y1 = c["start"]
            x2, y2 = c["end"]

            xs += [x1, x2]
            ys += [y1, y2]

        elif c["type"] == "arc":
            cx, cy = c["center"]
            r = c["radius"]

            xs += [cx - r, cx + r]
            ys += [cy - r, cy + r]

        elif c["type"] == "polyline":
            for x, y in c["points"]:
                xs.append(x)
                ys.append(y)

    return {
        "min_x": min(xs),
        "max_x": max(xs),
        "min_y": min(ys),
        "max_y": max(ys),
    }


def distance_from_center(contour, cx, cy):

    x, y = contour_center(contour)

    return math.hypot(x - cx, y - cy)


def apply_cut_order(contours):
    """
    Kolejność cięcia:
    - najpierw otwory
    - potem kontur zewnętrzny
    """

    if not contours:
        return contours

    bbox = compute_bbox(contours)

    sheet_cx = (bbox["min_x"] + bbox["max_x"]) / 2
    sheet_cy = (bbox["min_y"] + bbox["max_y"]) / 2

    # oznaczamy kontur zewnętrzny
    largest = max(contours, key=contour_size)

    for c in contours:
        c["outer"] = (c is largest)

    # sortowanie: otwory → zewnętrzny
    sorted_contours = sorted(
        contours,
        key=lambda c: (
            c["outer"],  # outer na końcu
            distance_from_center(c, sheet_cx, sheet_cy),
            contour_size(c)
        )
    )

    return sorted_contours