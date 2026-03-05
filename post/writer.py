def apply_markers(template, markers):

    for key, value in markers.items():

        template = template.replace(
            "{" + key + "}",
            str(value)
        )

    return template