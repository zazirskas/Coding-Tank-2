import random

numeros_loto = []
for i in range(15):
  num = random.randint(1, 100)
  while num in numeros_loto:
    num = random.randint(1, 100)
  numeros_loto.append(num)

pontos = 0
contador = 1
aposta = []

for i in range(15) :
    número = int(input('Insira 15 dezenas de 1 a 100: '))
    print('Você ja inseriu', contador , 'dezenas')
    while (número > 100 or número < 1) or (número in aposta) :
        número = int(input('número inserido não está entre 1 e 100 ou já foi inserido, insira novamente: '))
    aposta.append(número)
    contador += 1

for i in range(15) :
    if aposta[i] in numeros_loto :
        pontos += 1

if pontos == 15 :
    print('Você marcou', pontos, 'pontos e ganhou R$1 milhão')
elif pontos == 14 or pontos == 13 :
    print('Você marcou', pontos, 'pontos e ganhou R$100 mil')
elif pontos <= 12 and pontos >= 10 :
    print('Você marcou', pontos, 'pontos e ganhou R$2 mil')
elif pontos < 10 :
    print('Você marcou', pontos, 'pontos e não há premiação')

print('Os números sorteados foram:', numeros_loto)
print('Seus números foram: ', aposta)