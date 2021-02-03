operações = {
    'if':'se',
    'while':'enquanto',
    '>':'maior que',
    '<':'menor que',
    '>=':'maior igual que',
    '<=':'menor igual que',
    '==':'igual a',
    '!=':'diferente que',
    'print':'imprima o valor da variável'
}

a_traduzir = input('')

if 'if' in a_traduzir or 'while' in a_traduzir or '>' in a_traduzir or '<' in a_traduzir or '>=' in a_traduzir or '<=' \
in a_traduzir or '==' in a_traduzir or '!=' in a_traduzir or 'print' in a_traduzir:
   traduzido = a_traduzir.replace('if', operações['if'])
   traduzido = traduzido.replace('while',operações['while'])
   traduzido = traduzido.replace('>', operações['>'])
   traduzido = traduzido.replace('<', operações['<'])
   traduzido = traduzido.replace('>=', operações['>='])
   traduzido = traduzido.replace('<=', operações['<='])
   traduzido = traduzido.replace('==', operações['=='])
   traduzido = traduzido.replace('!=', operações['!='])
   traduzido = traduzido.replace('print', operações['print'])
   traduzido = traduzido.replace('(', ' ')
   traduzido = traduzido.replace(')', '')

print(traduzido)