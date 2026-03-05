import math


def generate_toolpath(contours):

    lines = []
    n = 60

    for contour in contours:

        # =================
        # POLYLINE
        # =================

        if contour["type"] == "polyline":

            points = contour["points"]
            start = points[0]

            lines.append(f"N{n} X{start[0]:.3f} Y{start[1]:.3f}")
            n += 10

            lines.append(f"N{n} TC_LASER_ON(1)")
            n += 10

            for p in points[1:]:

                lines.append(f"N{n} G01 X{p[0]:.3f} Y{p[1]:.3f}")
                n += 10

            lines.append(f"N{n} TC_LASER_OFF(2)")
            n += 10


        # =================
        # CIRCLE
        # =================

        elif contour["type"] == "circle":

            cx, cy = contour["center"]
            r = contour["radius"]

            start_x = cx + r
            start_y = cy

            lines.append(f"N{n} X{start_x:.3f} Y{start_y:.3f}")
            n += 10

            lines.append(f"N{n} TC_LASER_ON(1)")
            n += 10

            lines.append(
                f"N{n} G02 X{start_x:.3f} Y{start_y:.3f} I{-r:.3f} J0.000"
            )
            n += 10

            lines.append(f"N{n} TC_LASER_OFF(2)")
            n += 10


        # =================
        # ARC
        # =================

        elif contour["type"] == "arc":

            cx, cy = contour["center"]
            r = contour["radius"]

            start_angle = math.radians(contour["start_angle"])
            end_angle = math.radians(contour["end_angle"])

            start_x = cx + r * math.cos(start_angle)
            start_y = cy + r * math.sin(start_angle)

            end_x = cx + r * math.cos(end_angle)
            end_y = cy + r * math.sin(end_angle)

            lines.append(f"N{n} X{start_x:.3f} Y{start_y:.3f}")
            n += 10

            lines.append(f"N{n} TC_LASER_ON(1)")
            n += 10

            lines.append(
                f"N{n} G02 X{end_x:.3f} Y{end_y:.3f} I{cx-start_x:.3f} J{cy-start_y:.3f}"
            )
            n += 10

            lines.append(f"N{n} TC_LASER_OFF(2)")
            n += 10

    return "\n".join(lines)