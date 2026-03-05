import ezdxf


def parse_dxf(file_path):

    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    geometry = []

    for entity in msp:

        if entity.dxftype() == "LINE":

            start = entity.dxf.start
            end = entity.dxf.end

            geometry.append({
                "type": "line",
                "start": (start.x, start.y),
                "end": (end.x, end.y)
            })


        elif entity.dxftype() == "CIRCLE":

            center = entity.dxf.center
            radius = entity.dxf.radius

            geometry.append({
                "type": "circle",
                "center": (center.x, center.y),
                "radius": radius
            })


        elif entity.dxftype() == "ARC":

            center = entity.dxf.center

            geometry.append({
                "type": "arc",
                "center": (center.x, center.y),
                "radius": entity.dxf.radius,
                "start_angle": entity.dxf.start_angle,
                "end_angle": entity.dxf.end_angle
            })


        elif entity.dxftype() == "LWPOLYLINE":

            points = []

            for p in entity.get_points():
                points.append((p[0], p[1]))

            geometry.append({
                "type": "polyline",
                "points": points,
                "closed": entity.closed
            })


    return geometry