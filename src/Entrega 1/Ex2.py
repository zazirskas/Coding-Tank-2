print('Sistema de diagnóstico automático, responda as perguntas com Sim ou Não')

def entrada_invalída(Resposta):
    while Resposta.lower() != 'sim' and Resposta.lower() != 'não' and Resposta.lower() != 'nao':
        Resposta = input('Resposta inválida, responda novamente com Sim ou Não: ')
    return Resposta.lower()

p1 = input('Sente dor no corpo? ')
if entrada_invalída(p1) == 'sim':
    p1 = 'sim'
else:
    p1 = 'nao'

p2 = input('Você tem febre? ')
if entrada_invalída(p2) == 'sim':
    p2 = 'sim'
else:
    p2 = 'nao'

p3 = input('Você tem tosse? ')
if entrada_invalída(p3) == 'sim':
    p3 = 'sim'
else:
    p3 = 'nao'

p4 = input('Está com congestão nasal? ')
if entrada_invalída(p4) == 'sim':
    p4 = 'sim'
else:
    p4 = 'nao'

p5 = input('Tem manchas pelo corpo? ')
if entrada_invalída(p5) == 'sim':
    p5 = 'sim'
else:
    p5 = 'nao'

if p1 == 'sim' and p2 == 'sim' and p5 == 'sim':
    print('Você está com Dengue')
elif p2 == 'sim' and p3 == 'sim' and p4 == 'sim':
    print('Você está com gripe')
elif p2 == 'nao' and p3 == 'nao' and p4 == 'nao':
    print('Você não possui doenças')