import random

opcoes = ['pedra', 'papel', 'tesoura']

aleatório_pc = random.randint(0, 2)

player = ''
continua = ''

while continua.lower() != 'n':
    player = input('Insira pedra, papel ou tesoura: ')
    while player.lower() != 'pedra' and player.lower() != 'tesoura' and player.lower() != 'papel':
        player = input('Opção inválida, escolha pedra, papel ou tesoura: ')
    aleatório_pc = random.randint(0, 2)
    print(f'A escolha do computador foi {opcoes[aleatório_pc]}')
    if player.lower() == 'pedra' and opcoes[aleatório_pc].lower() == 'tesoura':
        print('Pedra vence tesoura, você ganhou')
    elif player.lower() == 'tesoura' and opcoes[aleatório_pc].lower() == 'pedra':
        print('Pedra vence de tesoura, você perdeu')
    elif player.lower() == 'papel' and opcoes[aleatório_pc].lower() == 'pedra':
        print('Papel vence de pedra, você ganhou')
    elif player.lower() == 'pedra' and opcoes[aleatório_pc].lower() == 'papel':
        print('Papel vence de pedra, você perdeu')
    elif player.lower() == 'tesoura' and opcoes[aleatório_pc].lower() == 'papel':
        print('Tesoura vence papel, você ganhou')
    elif player.lower() == 'papel' and opcoes[aleatório_pc].lower() == 'tesoura':
        print('Tesoura vence papel, você perdeu')
    elif player.lower() == 'tesoura' and opcoes[aleatório_pc].lower() == 'tesoura':
        print('Vocês empataram, jogue novamente')
    elif player.lower() == 'pedra' and opcoes[aleatório_pc].lower() == 'pedra':
        print('Vocês empataram, jogue novamente')
    elif player.lower() == 'papel' and opcoes[aleatório_pc].lower() == 'papel':
        print('Vocês empataram, jogue novamente')
    continua = input('Deseja jogar novamente? (s/n): ')
    print('-------------------------\n')

