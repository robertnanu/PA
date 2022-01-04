st = [10, 78, 8051, 91]

def sum_cif(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s


def cifra_control(n):
    suma = sum_cif(n)
    while suma > 9:
        suma = sum_cif(suma)
    return suma


def insereaza_cifra_control(st):
    for x in st:
        print(x, cifra_control(x), end='\n')
    return

# insereaza_cifra_control(st)


def egale(x, y):
    if len(x) != len(y):
        return False
    i, j = 0, 0
    while i < len(x) and j < len(y):
        if x[i] != y[i]:
            return False
        i += 1
        j += 1
    return True

# print(egale([1, 2, 3], [1, 2, 3, 4]))

f = open("numere.in", "r")
x = f.readline().split()
x = [int(x[i]) for i in range(len(x))]
f.close()

def formeaza_vector_cifre_control(st, list):
    for x in st:
        list.append(cifra_control(x))
    return list


list1 = []
formeaza_vector_cifre_control(x, list1)
# print(list1)

f = open("numere.in", "r")
y = f.readline().split()
y = [int(x[i]) for i in range(len(x))]
f.close()

list2 = []
formeaza_vector_cifre_control(y, list2)
# print(list2)

if egale(list1, list2):
    print("da")
else:
    print("nu")