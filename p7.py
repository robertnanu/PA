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

print(cifra_control(129))
