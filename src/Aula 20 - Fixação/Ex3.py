def tamanho_lista(números):
    elemento = 1
    if len(números) == 1:
        return elemento
    else:
        return tamanho_lista(números[1:]) + elemento

adicionar_elemento = ''
ver_tamanho = []

while adicionar_elemento.lower() != 'sair':
    adicionar_elemento = input('Insira o elemento a ser inserido na lista, digite "Sair": ')
    if adicionar_elemento.lower() == 'sair':
       break 
    ver_tamanho.append(adicionar_elemento)

print(tamanho_lista(ver_tamanho))