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

def format_double_array_for_assembler(data):
    formatted_list = ""
    for i in range(len(data)):
        for j in range(len(data[i])):
            formatted_list += f" ${data[i][j]:02X},"
        formatted_list += " 255,"
    return formatted_list+" 254,"

def formatDoubleArray(data):
    lines = data.split("\n")
    array_data=[]
    for line in lines:
        if len(line) > 0:
            new_array=line.split(" ")
            new_array = [int(x) for x in new_array]
            array_data.append(new_array)

    return array_data