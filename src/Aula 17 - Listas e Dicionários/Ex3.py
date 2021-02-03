hub = {

    "SP" : {

        "RJ" : 30 ,
        "Curitiba" : 30 ,
        "BH" : 45
    } ,
}

rotas = {
    "RJ" : {
        
        "SP" : 30 ,
        "BH" : hub["SP"]["BH"] + hub["SP"]["RJ"] ,
        "Curitiba" : hub["SP"]["RJ"] + hub["SP"]["Curitiba"]
    } ,

    "BH" : {

        "SP" : 45,
        "Curitiba" : 75,
        "RJ" : hub["SP"]["BH"] + hub["SP"]["RJ"]

    },

    "Curitiba" : {

        "SP" : 30 ,
        "BH" : 75 ,
        "RJ" : hub["SP"]["Curitiba"] + hub["SP"]["RJ"]
    },

    "SP" : {

        "RJ" : 30 ,
        "Curitiba" : 30 ,
        "BH" : 45
    }

}

origem = input('Digite a origem da viagem (SP,BH,RJ ou Curitiba): ')

while origem != 'SP' and origem != 'BH' and origem != 'RJ' and origem != 'Curitiba':
    origem = input('Origem da viagem inválida digite novamente: ')

destino = input('Digite o destino da viagem (SP,BH,RJ ou Curitiba): ')

while destino != 'SP' and destino != 'BH' and destino != 'RJ' and destino != 'Curitiba':
    destino = input('destino da viagem inválida digite novamente: ')

preço_da_viagem = rotas[origem][destino] * 12.75
print(rotas[origem][destino])

print('O preço da rota', origem, 'x' , destino , 'é:', "R$", preço_da_viagem)
    