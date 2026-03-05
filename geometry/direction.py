import math


def polygon_area(points):

    area = 0

    n = len(points)

    for i in range(n):

        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]

        area += (x1 * y2 - x2 * y1)

    return area / 2


def detect_direction(contours):

    for c in contours:

        if c["type"] == "polyline":

            area = polygon_area(c["points"])

            if area > 0:
                c["direction"] = "CCW"
            else:
                c["direction"] = "CW"

        elif c["type"] == "circle":

            if c.get("outer", False):
                c["direction"] = "CCW"
            else:
                c["direction"] = "CW"

        elif c["type"] == "arc":

            start = c["start_angle"]
            end = c["end_angle"]

            delta = end - start

            if delta > 0:
                c["direction"] = "CCW"
            else:
                c["direction"] = "CW"

        elif c["type"] == "line":

            # linia sama nie ma kierunku
            c["direction"] = "NONE"

    return contours