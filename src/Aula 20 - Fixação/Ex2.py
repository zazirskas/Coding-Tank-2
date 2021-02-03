#Função base do enunciado

def H(n, m):
  x = n
  y = x
  while x < m:
    x = x + 1
    y = y + x
  return y

#Resposta exercício 2
def F(n, m):
    x = n
    valor_atual = n+1
    if x == m:
        return m
    else:
        return F(valor_atual, m) + n


print(F(1,10))


