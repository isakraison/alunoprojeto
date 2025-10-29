def cadastro():
    nome=input('digite seu nome:')
    cpf=input('digite seu cpf:')
    endereço=input('digite seu endereço:')
    idade=int(input('digite sua idade:'))
   

    print('\n--- FICHA DE CADASTRO ---')

    print('seu nome é:',nome)
    print('seu cpf é:',cpf)
    print('seu endereço é:',endereço)
    print('sua idade é:',idade)

    if idade<18:
        print('você é menor de idade,você não pode se cadastrar')
    else:
        print('você é maior de idade\n,cadastro realizado com sucesso')

cadastro()

