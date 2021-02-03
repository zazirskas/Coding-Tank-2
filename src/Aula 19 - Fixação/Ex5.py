def fatorial(N) :
    if N == 0 :
        return 0

    elif N == 1 :
        return 1

    else:
        return N * fatorial(N-1)


Número = int(input('Insira o número que deseja calcular o fatorial: '))

print(fatorial(Número))