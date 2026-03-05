import matplotlib.pyplot as plt
import math


def draw_circle(ax, cx, cy, r, color="black"):
    circle = plt.Circle((cx, cy), r, fill=False, color=color)
    ax.add_patch(circle)


def draw_lead(ax, start, lead_start):

    x1, y1 = lead_start
    x2, y2 = start

    ax.plot([x1, x2], [y1, y2], color="green")


def draw_pierce(ax, point):

    x, y = point

    ax.plot(x, y, marker="o", color="red")


def generate_preview(contours, bbox, output_path):

    fig, ax = plt.subplots(figsize=(10, 5))

    # arkusz
    sheet_x = 3000
    sheet_y = 1500

    ax.set_xlim(0, sheet_x)
    ax.set_ylim(0, sheet_y)

    # podziałka
    ax.set_xticks(range(0, sheet_x + 1, 200))
    ax.set_yticks(range(0, sheet_y + 1, 100))

    ax.grid(True)

    # rysowanie konturów
    for c in contours:

        if c["type"] == "circle":

            cx, cy = c["center"]
            r = c["radius"]

            draw_circle(ax, cx, cy, r)

            if "lead_start" in c:

                draw_lead(ax, c["start"], c["lead_start"])
                draw_pierce(ax, c["lead_start"])

    # bounding box
    min_x = bbox["min_x"]
    max_x = bbox["max_x"]
    min_y = bbox["min_y"]
    max_y = bbox["max_y"]

    rect_x = [min_x, max_x, max_x, min_x, min_x]
    rect_y = [min_y, min_y, max_y, max_y, min_y]

    ax.plot(rect_x, rect_y, linestyle="--", color="blue")

    # opis
    width = bbox["width"]
    height = bbox["height"]

    scrap_x = width + 20
    scrap_y = height + 20

    ax.set_title(
        f"Part size: {width:.1f} x {height:.1f} mm | Required scrap: {scrap_x:.1f} x {scrap_y:.1f} mm"
    )

    ax.set_aspect("equal")

    plt.savefig(output_path, dpi=200)
    plt.close()