st = "aorectc aropozitip este aceasta"

def deviruseaza(st):
    final = ''

    for x in st.split():
        if len(x) > 1:
            final += x[len(x) - 1]
            final += x[1:len(x) - 1]
            final += x[0]
            final += ' '
        else:
            final += x
            final += ' '

    vector = []
    for x in final.split():
        vector.append(x)

    aux = ''
    for x in range(0, len(vector) // 2):
        vector[x], vector[len(vector) - x - 1] = vector[len(vector) - x - 1], vector[x]

    final = ''
    for x in vector:
        final += x
        final += ' '

    return final

print(deviruseaza(st))