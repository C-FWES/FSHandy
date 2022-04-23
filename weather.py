
def format_runways(runways):
    formatted = []
    for r in runways:
        length = str(r['length_ft'])
        ident_1 = r['ident1']
        ident_2 = r['ident2']
        result_str = ident_1 + "/" + ident_2 + ": " + length + " feet"
        formatted.append(result_str)
    return formatted