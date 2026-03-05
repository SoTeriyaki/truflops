TECH_TABLE = {

    # OCYNK
    ("OC",2): "SS020MD0-N2SO-30-2",

    # NIERDZEWKA
    ("SN",1): "ST004MD0-O2SO-30-2",
    ("SC",6): "ST006MD0-O2SO-30-2",


    # CZARNA
    ("SN",1.5): "SS015MD0-N2SO-30-2",
    ("SN",2): "SS020MD0-N2SO-30-2"

}

def get_tech_name(material, thickness):

    key = (material, thickness)

    if key not in TECH_TABLE:
        raise RuntimeError("Brak technologii dla materiału")

    return TECH_TABLE[key]