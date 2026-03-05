import math


def apply_leads(contours, lead_length=1.5):

    for c in contours:

        if c["type"] != "circle":
            continue

        cx, cy = c["center"]
        r = c["radius"]

        direction = c.get("direction", "CCW")

        # punkt startowy na konturze (na osi X)
        sx = cx + r
        sy = cy

        # punkt startowy lead-in (trochę na zewnątrz)
        if direction == "CW":
            lx = sx + lead_length
            ly = sy
        else:
            lx = sx + lead_length
            ly = sy

        c["start"] = (sx, sy)
        c["lead_start"] = (lx, ly)

    return contours