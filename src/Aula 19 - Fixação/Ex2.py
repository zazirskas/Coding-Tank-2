
def repetidos_lista() :
    lista = []
    item  = input('Insira o número a ser incluído na lista, digite "sair" para parar de inserir : ')
    cont = 0

    while item.lower() != "sair" :
        lista.append(int(item))
        item  = input('Insira o número a ser incluído na lista, digite "sair" para parar de inserir : ')

    for itens in lista :
        if lista.count(itens) == 1 :
            cont += 1
            
    print(f'Existem {cont} números sem repetição')

repetidos_lista()
