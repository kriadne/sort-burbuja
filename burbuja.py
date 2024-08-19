lista = [200, 419, 6, 2, 49, 1, 38]
loops = 0

for i in range(len(lista)):
    for ii in range(len(lista)-i-1):
        if lista[ii] > lista[ii+1]:
            aux = lista[ii]
            lista[ii] = lista[ii+1]
            lista[ii+1] = aux
        loops += 1

# lista.sort()

print(lista)
print(loops)
