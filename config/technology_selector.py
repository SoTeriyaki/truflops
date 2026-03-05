TECH_TABLE = {

    ("SC",4): "ST004MD0-O2SO-30-2",
    ("SC",6): "ST006MD0-O2SO-30-2",

    ("SN",1.5): "SS015MD0-N2SO-30-2",
    ("SN",2): "SS020MD0-N2SO-30-2"

}

def get_tech_name(material, thickness):

    key = (material, thickness)

    if key not in TECH_TABLE:
        raise RuntimeError("Brak technologii dla materiału")

    return TECH_TABLE[key]