ls = [3, -3, 1, 7, 3, 2]
m = []

def min_max(ls):
    return min(ls), max(ls)

def incarcare(fisier):
    f = open(fisier, 'r')
    for line in f.readlines():
        m.append(line.split())
    f.close()

    x = []

    for i in m:
        x.append([int(numeric_string) for numeric_string in i])
    
    return x

fisier_citire = input("Din ce fisier vom prelua datele de intrare?\n")

x = incarcare(fisier_citire)

ok = 0 # presupunem ca nu exista o astfel de linie
indice = -1

for i in x:
    indice += 1
    x, y = min_max(i)
    if x == y:
        ok = 1
        print(indice)

if not ok:
    print("Nu exista!")