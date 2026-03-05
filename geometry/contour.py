import math

TOLERANCE = 0.001


def points_equal(p1, p2):
    return (
        abs(p1[0] - p2[0]) < TOLERANCE and
        abs(p1[1] - p2[1]) < TOLERANCE
    )


def build_contours(geometry):

    contours = []
    lines = []

    for g in geometry:

        if g["type"] == "line":
            lines.append({
                "start": g["start"],
                "end": g["end"]
            })

        elif g["type"] == "circle":

            contours.append({
                "type": "circle",
                "center": g["center"],
                "radius": g["radius"]
            })

        elif g["type"] == "arc":

            contours.append({
                "type": "arc",
                "center": g["center"],
                "radius": g["radius"],
                "start_angle": g["start_angle"],
                "end_angle": g["end_angle"]
            })

    # składanie linii w kontury
    while lines:

        current = lines.pop(0)
        contour = [current["start"], current["end"]]

        extended = True

        while extended:

            extended = False

            for line in lines:

                if points_equal(contour[-1], line["start"]):

                    contour.append(line["end"])
                    lines.remove(line)
                    extended = True
                    break

                elif points_equal(contour[-1], line["end"]):

                    contour.append(line["start"])
                    lines.remove(line)
                    extended = True
                    break

        contours.append({
            "type": "polyline",
            "points": contour
        })

    return contours