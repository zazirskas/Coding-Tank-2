
contador = 0

cadastrados = { 
    'joao' : {} ,
    'fernando' : {}
    }

print('1 - Cadastrar')
print('2 - Visualizar os cadastrados')
print('3 - Buscar um cadastro específico')
print('4 - Sair')

opcao = int(input('Insira a opção desejada: '))

while opcao > 4 or opcao < 1 :
    opcao = int(input('Opção inválida, insira novamente: '))

while opcao >= 1 or opcao <= 4:    
    
    while opcao > 4 or opcao < 1 :
        opcao = int(input('Opção inválida, insira novamente: '))

    if opcao == 1 :
        print('-----------Cadastro inicializado------------')
        cpf = input('Insira o CPF da pessoa a ser cadastrado (xxx.xxx.xxx-xx): ')
        nome1 = input('Insira o primeiro nome da pessoa a ser cadastrada: ')
        nome2 = input('Insira o sobrenome da pessoa a ser cadastrada: ')
        idade = int(input('Insira a idade da pessoa a ser cadastrada: '))
        email = input('Insira o email da pessoa a ser cadastrada: ')
        cadastrados.update({ 
            cpf : { 
                'nome' : nome1 ,
                'sobrenome' : nome2,
                'idade' : idade,
                'email' : email,
                }})
        print('---------Cadastro finalizado-----------')
        print('1 - Cadastrar')
        print('2 - Visualizar os cadastrados')
        print('3 - Buscar um cadastro específico')
        print('4 - Sair')
        opcao = int(input('Insira uma nova opção: '))

    elif opcao == 2 :
        print('----------Visualizar cadastrados iniciado----------')
        for cadastros in cadastrados :
            print(cadastros)
            contador +=1
            if contador == len(cadastrados) :
                print('---------Visualizar cadastrados finalizado-----------')
                print('1 - Cadastrar')
                print('2 - Visualizar os cadastrados')
                print('3 - Buscar um cadastro específico')
                print('4 - Sair')
                opcao = int(input('Insira uma nova opção: '))
    
    elif opcao == 3:
        print('------------Buscar cadastro iniciado------------')
        busca = input('Digite o CPF do cadastro desejado (xxx.xxx.xxx-xx): ')
        print(cadastrados[busca])
        print('------------Buscar cadastro finalizado------------')
        print('1 - Cadastrar')
        print('2 - Visualizar os cadastrados')
        print('3 - Buscar um cadastro específico')
        print('4 - Sair')
        opcao = int(input('Insira uma nova opção: '))
    
    elif opcao == 4 :
        print('-----------Programa finalizado-----------')
        exit