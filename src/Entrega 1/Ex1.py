print('Responda o questionário da polícia com Sim ou Não')
pontos = 0

def entrada_invalída(Resposta):
    while Resposta.lower() != 'sim' and Resposta.lower() != 'não' and Resposta.lower() != 'nao':
        Resposta = input('Resposta inválida, responda novamente com Sim ou Não: ')
    return Resposta.lower()


p1 = input('Mora perto da vítima?: ')
if entrada_invalída(p1) == 'sim':
    pontos += 1

p2 = input('Já trabalhou com a vítima?: ')
if entrada_invalída(p2) == 'sim':
    pontos += 1

p3 = input('Telefonou para a vítima?: ')
if entrada_invalída(p3) == 'sim':
    pontos += 1

p4 = input('Esteve no local do crime?: ')
if entrada_invalída(p4) == 'sim':
    pontos += 1

p5 = input('Devia para a vítima?: ')
if entrada_invalída(p5) == 'sim':
    pontos += 1

if pontos == 5:
    print('Você é o assassino')
elif pontos <= 4 and pontos >= 3:
    print('Você é cúmplice') 
elif pontos == 2:
    print('Você é suspeito')
elif pontos <= 1:
    print('Você está liberado') 