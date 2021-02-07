creches = {
    "Recanto do Sol" : {
        "cachorros": 12,
        "gatos": 4,
        "coelhos": 2,
    },
    "Lar dos bichos" : {
        "cachorros": 8,
        "gatos": 5,
        "porquinhos-da-índia": 3,
    },
    "A Fazenda" : {
        "cachorros": 20,
        "coelhos": 10,
    },
    "Casa da Alegria" : {
        "gatos": 15,
        "porquinhos-da-índia": 7,
    },
}

quantidade_de_animais_por_especie = {
    "Cachorros" : creches["Recanto do Sol"]["cachorros"] + creches["Lar dos bichos"]["cachorros"] + creches["A Fazenda"]["cachorros"],
    "Gatos" : creches["Recanto do Sol"]["gatos"] + creches["Lar dos bichos"]["gatos"] + creches["Casa da Alegria"]["gatos"],
    "Coelhos" : creches["Recanto do Sol"]["coelhos"] + creches["A Fazenda"]["coelhos"],
    "Porquinhos-da-índia" : creches["Lar dos bichos"]["porquinhos-da-índia"] + creches["Casa da Alegria"]["porquinhos-da-índia"]

}

continua = ''
print('------- Programa de consolidação de animais ------')

for animais in quantidade_de_animais_por_especie:
    print(animais, quantidade_de_animais_por_especie[animais])

