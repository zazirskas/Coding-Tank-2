def inverter_palavra(palavra):
    indice_atual = len(palavra) - 1
    if len(palavra) == 1:
        return palavra[indice_atual]
    else:
        return inverter_palavra(palavra[1:]) + palavra[0]

frase = input('Insira a frase que deseja inverter: ')
print(inverter_palavra(frase))