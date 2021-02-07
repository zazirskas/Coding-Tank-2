lista_numeros = []

inserir_numero = ''

while len(lista_numeros) != 10:
    inserir_numero = input('Insira o número desejado na lista: ')
    while inserir_numero.isdigit() == False:
        inserir_numero = input('Entrada inválida, digite um número válido: ')
    lista_numeros.append(int(inserir_numero))

for elemento in lista_numeros:
    if elemento % 2 == 0:
        pass
    elif elemento % 5 == 0:
        pass
    else:
        lista_numeros.remove(elemento)

print('Os números divisiveis por 2 e 5 nesta lista são: ', lista_numeros)