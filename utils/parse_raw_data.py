def process_minus(filename):
    elements = []
    current_element = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('>tr') and line.endswith('SV=1\n'):
                if current_element:
                    elements.append(''.join(current_element))
                    current_element = []
            else:
                current_element.append(line.strip())

    if current_element:
        elements.append(''.join(current_element))

    return elements


def process_plus(filename):
    result = []
    with open(filename, 'r') as file:
        lines = file.readlines()

    current_element = ''
    for line in lines:
        line = line.strip()
        if line.startswith('>'):
            if current_element:
                result.append(current_element.rstrip('*'))
                current_element = ''
        else:
            current_element += line

    if current_element:
        result.append(current_element.rstrip('*'))

    return result