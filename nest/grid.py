SHEET_WIDTH = 3000
SHEET_HEIGHT = 1500

SCRAP = 30

SPACING_X = 10
SPACING_Y = 10


def generate_grid_nest(bbox, quantity):

    part_w = bbox["width"]
    part_h = bbox["height"]

    pitch_x = part_w + SPACING_X
    pitch_y = part_h + SPACING_Y

    usable_w = SHEET_WIDTH - SCRAP
    usable_h = SHEET_HEIGHT - SCRAP

    cols = int(usable_w // pitch_x)
    rows = int(usable_h // pitch_y)

    placements = []
    count = 0

    for r in range(cols):
        
        for c in range(rows):

            if count >= quantity:
                return placements

            x = SCRAP + c * pitch_x
            y = SCRAP + r * pitch_y

            placements.append({
                "x": x,
                "y": y
            })

            count += 1

    return placements