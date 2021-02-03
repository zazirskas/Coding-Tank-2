L = [6, 5, 34, -2, 3]

def retorna_mínimo(lista):
    menor_número = lista[0]
    if len(lista) == 1:
        return lista[0]
    else:
        return min(retorna_mínimo(lista[1:]), menor_número)

print(retorna_mínimo(L))