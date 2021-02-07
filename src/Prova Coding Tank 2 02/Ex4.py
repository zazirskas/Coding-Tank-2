import random
import string

letras_maisculas = string.ascii_uppercase # string com todas as letras maiscúlas de A a Z

letras = string.ascii_letters

num = random.randint(0, 9) # número aleatório entre 0 e 5.

random.random() #retorna um float aleatorio entre 0 e 1

def gerar_senha():
    aleatorio = ""
    senha = ''
    cont = 0
    quantidade_letras = int(input('Insira quantas letras você deseja na sua senha: '))
    quantidade_números = int(input('Insira quantos números você deseja na sua senha: '))
    while cont != quantidade_letras:
        aleatorio = random.choice(letras)
        senha = aleatorio + senha
        cont += 1
    cont = 0
    while cont != quantidade_números:
        num = random.randint(0, 9)
        senha = str(num) + senha
        cont += 1
    print(senha)
gerar_senha()
