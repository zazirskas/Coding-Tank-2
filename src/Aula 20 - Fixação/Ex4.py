def pesquisaLista(lista, número):
    item_atual = len(lista) - 1
    if int(lista[item_atual]) == número:
        return True
    elif int(lista[item_atual]) != número:
        atualização_tamanho = len(lista) - 1
        if atualização_tamanho == 0 :
            return False
        else:
            return pesquisaLista(lista[:atualização_tamanho], número)

adicionar_elemento = ''
lista_números = []

while adicionar_elemento.lower() != 'sair':
    adicionar_elemento = input('Insira o elemento a ser inserido na lista, digite "Sair": ')
    if adicionar_elemento.lower() == 'sair':
       break 
    lista_números.append(adicionar_elemento)

pesquisa = int(input('Insira o número que deseja checar se está na lista: '))

print(pesquisaLista(lista_números, pesquisa))