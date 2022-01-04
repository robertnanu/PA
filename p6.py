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

numar_maxim = 0

def prime(n, numar_maxim):
    final = []
    if not numar_maxim:
        return "Numar_maxim are valoarea 0"

    if numar_maxim != 0:
        for i in range(2, n):
            ok = 1
            for j in range(2, i):
                if i % j == 0:
                    ok = 0
            if ok == 1:
                final.append(i)
                numar_maxim -= 1
                if numar_maxim == 0:
                    break
    return final

m = []

def incarcare(fisier):
    f = open(fisier, 'r')
    for line in f.readlines():
        m.append(line.split())
    f.close()
    
    return m

g = open("intrare_devirusata.out", "w")

print(incarcare("intrare.in"))
contor = 0
for x in m:
    contor += 1
    if contor in prime(len(m)+1, len(m)):
        list = ''
        for i in x:
            list += i
            list += ' '
        g.write(deviruseaza(list))
        g.write('\n')
    else:
        list = ''
        for i in x:
            list += i
            list += ' '
        g.write(list)
        g.write('\n')

g.close()