import ezdxf
import tempfile


def parse_dxf(file_path):

    doc = ezdxf.readfile(file_path)

    # konwersja do R12
    r12_doc = ezdxf.new("R12")
    r12_msp = r12_doc.modelspace()

    for e in doc.modelspace():
        try:
            r12_msp.add_entity(e.copy())
        except:
            pass

    # zapis tymczasowy
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".dxf")
    r12_doc.saveas(temp_file.name)

    doc = ezdxf.readfile(temp_file.name)
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

            geometry.append({
                "type": "circle",
                "center": (center.x, center.y),
                "radius": entity.dxf.radius
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