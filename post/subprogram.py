import math


def generate_subprogram(contours):

    lines = []
    n = 100

    for contour in contours:

        # ---------- LEAD START ----------
        if "lead_start" in contour:

            x, y = contour["lead_start"]
            lines.append(f"N{n} G00 X{round(x,3)} Y{round(y,3)}")
            n += 10

            lines.append(f"N{n} TC_PCS_PIERCE")
            n += 10

        # ---------- START POINT ----------
        if "start" in contour:

            x, y = contour["start"]
            lines.append(f"N{n} G01 X{round(x,3)} Y{round(y,3)}")
            n += 10

        # ---------- CIRCLE ----------
        if contour["type"] == "circle":

            cx, cy = contour["center"]
            r = contour["radius"]

            start_x = cx + r
            start_y = cy

            lines.append(
                f"N{n} G03 I{round(cx-start_x,3)} J{round(cy-start_y,3)}"
            )
            n += 10

        # ---------- POLYLINE ----------
        elif contour["type"] == "polyline":

            for x, y in contour["points"]:

                lines.append(
                    f"N{n} G01 X{round(x,3)} Y{round(y,3)}"
                )
                n += 10

        # ---------- ARC ----------
        elif contour["type"] == "arc":

            cx, cy = contour["center"]
            start = contour["start"]
            end = contour["end"]

            i = cx - start[0]
            j = cy - start[1]

            lines.append(
                f"N{n} G03 X{round(end[0],3)} Y{round(end[1],3)} I{round(i,3)} J{round(j,3)}"
            )
            n += 10

        # ---------- LASER OFF ----------
        lines.append(f"N{n} TC_LASER_OFF(2)")
        n += 10

    return "\n".join(lines)