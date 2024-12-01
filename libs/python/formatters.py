def formatDataLinesWithSpace (data):
    lines = data.splitlines()
    lista = []
    listb = []
    for i in lines:
        i=i.replace('   ', ',')
        values = i.split(',')
        lista.append(int(values[0]))
        listb.append(int(values[1]))
    return lista, listb

def format_integers_for_assembler(int_list):
    formatted_list = ""
    for n in int_list:
        # Extract upper and lower 16 bits
        upper = (n >> 16) & 0xFFFF
        lower = n & 0xFFFF
        # Format for assembler: db $FFFF, $0000
        formatted_list+=f" ${upper:04X}, ${lower:04X},"
    return formatted_list