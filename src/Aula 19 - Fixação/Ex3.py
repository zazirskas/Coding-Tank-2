def lista_indeterminada(lista, item) :
    maior_numero = 0

    while item.lower() != "sair" :
        lista.append(int(item))
        item  = input('Insira o número a ser incluído na lista, digite "Sair" para parar de inserir : ')
    
    for itens in lista :
        if itens > maior_numero :
            maior_numero = itens
    return maior_numero
    
lista = []
item  = input('Insira o número a ser incluído na lista, digite "Sair" para parar de inserir : ')

print(f'O maior número desta lista é: {lista_indeterminada(lista, item)}')
    