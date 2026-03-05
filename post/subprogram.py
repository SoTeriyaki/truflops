def generate_toolpath(contours):

    lines = []

    n = 60  # numeracja linii jak w TruTops

    for contour in contours:

        start = contour[0]

        # szybki przejazd do startu
        lines.append(f"N{n} X{start[0]:.3f} Y{start[1]:.3f}")
        n += 10

        # włączenie lasera
        lines.append(f"N{n} TC_LASER_ON(1)")
        n += 10

        # cięcie
        for point in contour[1:]:

            lines.append(f"N{n} G01 X{point[0]:.3f} Y{point[1]:.3f}")
            n += 10

        # wyłączenie lasera
        lines.append(f"N{n} TC_LASER_OFF(2)")
        n += 10

    return "\n".join(lines)