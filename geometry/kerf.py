def apply_kerf(contours, kerf=0.1):

    half = kerf / 2

    if len(contours) == 0:
        return contours

    # największy kontur = zewnętrzny
    max_r = max(c["radius"] for c in contours if c["type"] == "circle")

    new_contours = []

    for c in contours:

        if c["type"] == "circle":

            r = c["radius"]

            if r == max_r:
                # kontur zewnętrzny
                r = r + half
            else:
                # otwór
                r = r - half

            new_contours.append({
                **c,
                "radius": r
            })

        else:
            new_contours.append(c)

    return new_contours