import random

num_sorteado = random.randint(1, 100)

def chute() :
    número = int(input('Insira o seu palpite de 1 a 100: '))
    while número != num_sorteado :
        if número > num_sorteado :
            print('Chute muito alto')
            número = int(input('Insira o seu palpite: '))
        elif número < num_sorteado :
            print('Chute muito baixo')
            número = int(input('Insira o seu palpite:'))
    print('Você acertou o número')

chute()