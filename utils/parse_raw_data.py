def process(filename):
    with open(filename, 'r') as file:
        data = [i.rstrip("\n") for i in file.readlines()]
    
    result_proteins = []
    protein = ""

    for item in data:
        if item.startswith(">"):
            result_proteins.append(protein)
            protein = ""
        else:
            protein += item.rstrip("*")
    
    return result_proteins
