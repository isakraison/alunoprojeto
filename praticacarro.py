def carro():
    ano=input('digite o ano do carro:')
    modelo=input('digite o modelo do carro:')
    cor=input('digite a cor do carro:')
    rodas=int(input('digite o numero de rodas:'))

    print('\n--- CARRO ---')

    print('o ano do carro é:',ano)
    print('o modelo do carro é:',modelo)
    print('a cor do carro é:',cor)
    print('o carro tem ',rodas)

    if rodas > 4:
        print('é um caminhão ou carreta')
    else:
        print('é um carro normal')

carro()
