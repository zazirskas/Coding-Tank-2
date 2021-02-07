def fibonacci(posição):
    if posição == 1:
        return 0
    elif posição == 2:
        return 1
    else:
        atualizador = posição - 1
        return fibonacci(atualizador) + fibonacci(atualizador-1)

print(fibonacci(9))