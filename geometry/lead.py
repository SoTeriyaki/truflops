import math


LEAD_RADIUS = 1.5


def add_lead_in(contour):

    if contour["type"] == "circle":

        cx, cy = contour["center"]
        r = contour["radius"]

        start_x = cx + r
        start_y = cy

        lead_start_x = cx + r + LEAD_RADIUS
        lead_start_y = cy

        return {
            "type": "circle",
            "center": (cx, cy),
            "radius": r,
            "lead_start": (lead_start_x, lead_start_y),
            "start": (start_x, start_y)
        }

    elif contour["type"] == "polyline":

        points = contour["points"]

        p0 = points[0]
        p1 = points[1]

        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]

        length = math.hypot(dx, dy)

        if length == 0:
            return contour

        nx = -dy / length
        ny = dx / length

        lead_start = (
            p0[0] + nx * LEAD_RADIUS,
            p0[1] + ny * LEAD_RADIUS
        )

        contour["lead_start"] = lead_start
        contour["start"] = p0

        return contour

    return contour


def apply_leads(contours):

    result = []

    for c in contours:
        result.append(add_lead_in(c))

    return result