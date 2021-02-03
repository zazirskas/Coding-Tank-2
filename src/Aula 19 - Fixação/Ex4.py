def contagem(N) :
    if N == 1  :
        return N
    else:
        print(N)
        return contagem(N - 1)

N = int(input('Insira até o número que deseja contar: '))
print(contagem(N))