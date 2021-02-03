def somaLista(lista) :

    if len(lista) == 1 :
        return lista[0]
    else:
        return lista[0] + somaLista(lista[1:])

lista = [1,2,3,4,5]

print(somaLista(lista))