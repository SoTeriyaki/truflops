TECH_TABLE = {

    # OCYNK
    ("OC",2): "SS020MD0-N2SO-30-2",

    # NIERDZEWKA
    ("SN",1): "SS010MDO-N2SO-30-2",
    ("SN",1.5): "SS015MDO-N2SO-30-2",
    ("SN",2): "SS020MDO-N2SO-30-2",
    ("SN",3): "SS030MDO-N2SO-30-2",
    ("SN",4): "SS040MDO-N2SO-30-2",
    ("SN",5): "SS050MDO-N2SO-30-2",


    # CZARNA
    ("SN",1.5): "SS015MD0-N2SO-30-2",
    ("SN",2): "SS020MD0-N2SO-30-2"

}

def get_tech_name(material, thickness):

    key = (material, thickness)

    if key not in TECH_TABLE:
        raise RuntimeError("Brak technologii dla materiału")

    return TECH_TABLE[key]