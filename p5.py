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
                # print(i, end=' ')
                final.append(i)
                numar_maxim -= 1
                if numar_maxim == 0:
                    break
    return final

print(prime(15, 7))