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
    "Cachorros" : creches["Recanto do Sol"]["cachorros"] + creches["Lar dos bichos"]["cachorros"] + creches["A Fazenda"]["cachorros"] + creches["Casa da Alegria"]["cachorros"],
    "Gatos" : creches["Recanto do Sol"]["gatos"] + creches["Lar dos bichos"]["gatos"] + creches["A Fazenda"]["gatos"] + creches["Casa da Alegria"]["gatos"],
    "Coelhos" : creches["Recanto do Sol"]["coelhos"] + creches["Lar dos bichos"]["coelhos"] + creches["A Fazenda"]["coelhos"] + creches["Casa da Alegria"]["coelhos"],
    "Coelhos" : creches["Recanto do Sol"]["porquinhos-da-índia"] + creches["Lar dos bichos"]["porquinhos-da-índia"] + creches["A Fazenda"]["porquinhos-da-índia"] + creches["Casa da Alegria"]["porquinhos-da-índia"]

}

continua = ''
print('------- Programa de controle de animais ------')

while continua != 'n' and continua != '5':
    print('----------------------')
    print('1 - Cadastrar abrigo')
    print('2 - Cadastrar tipo de animal')
    print('3 - Inserir quantidade de animais: ')
    print('4 - Visualizar animais disponíveis em todos os abrigos')
    print('5 - Sair')
    continua = input('Insira a opção desejada: ')
    print('-----------------\n')
    if continua == '1':
        nome_abrigo = input('Insira o nome do abrigo a ser cadastrado: ')
        creches.update({ nome_abrigo : {}})
    if continua == '2':
        abrigos = list(creches.keys())
        print(abrigos[0])
        espécie = input('Insira a espécie a cadastrar: ')
        nome_abrigo = input('Insira o nome do abrigo que deseja cadastrar a espécie: ')
        creches[nome_abrigo].update({ espécie : 0 })
    if continua == '3':
        abrigos = list(creches.keys())
        print(abrigos[0])
        nome_abrigo = input('Insira o nome do abrigo que deseja cadastrar a espécie: ')
        espécie = input('Insira a qual espécie deseja editar quantidade: ')
        quantidade = input('Insira a quantidade da espécie: ')
        creches[nome_abrigo].update({ espécie : quantidade })
    if continua == '4'

