m = []

def incarcare(fisier):
    f = open(fisier, 'r')
    for line in f.readlines():
        m.append(line.split())
    f.close()

    x = []

    for i in m:
        x.append([int(numeric_string) for numeric_string in i])
    
    return x

print(incarcare("incarcare_fisier"))