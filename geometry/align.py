from geometry.bbox import compute_bbox
from geometry.transform import translate_geometry


def align_to_origin(geometry):

    bbox = compute_bbox(geometry)

    dx = -bbox["min_x"]
    dy = -bbox["min_y"]

    return translate_geometry(geometry, dx, dy)