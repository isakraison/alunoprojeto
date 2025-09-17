

def aluno():
    idade=int(input('digite a sua idade:'))
    
    if idade >18:
        print('você é um ex aluno,e não tem acesso as suas notas e as atividades')
    else:
        nome=input('digite o seu nome completo:')
    sala = int(input('digite seu curso:' \
        '\n1-enfermagem' \
        '\n2-desenvolvimento de sistemas' \
        '\n3-finanças' \
        '\n4-administração'))
    if sala ==1:
        print('você é de enfermagem')
    if sala==2:
        print('você é de desenvolvimento de sistemas')
    if sala==3:
        print('você é de finanças')
    if sala ==4:
        print('você é de administração')
        turno=input('digite qual seu turno:')
        serie=input('digite qual sua serie::')
        print('você é um aluno em atividade!\ndigite suas notas a seguir e veja se passou de ano')
        



        def notas():


            n1=float(input('digite sua nota do primeiro bimestre para calcular a media :'))
            n2=float(input('digite sua nota do segundo bimestre para calcular a media :'))
            n3=float(input('digite sua nota do terceiro bimestre para calcular a media :'))
            n4=float(input('digite sua nota do quarto bimestre para calcular a media :'))

            media=(n1+n2+n3+n4)/4
            mfinal=media
            if media >6:
                print('você passou de ano!')
            else:
                print('sua nota final é:',mfinal)
        notas()

        print('agora escolha o almoço que você quer comer:')
        print('digite 1 para frango assado\ndigite 2 para lasanha \ndigite 3 para macarronada\ndigite 4 para feijoada\ndigite 5 para urea de jumento')
        opção=int(input('escolha uma das opções.'))

        if opção==1:
            print('você escolheu almoçar frango assado')
        if opção==2:
            print('você escolheu almoçar lasanha')
        if opção==3:
            print('você escolheu almoçar macarronada')
        if opção==4:
            print('você escolheu almoçar feijoada')
        if opção==5:
            print('você escolheu almoçar urea de jumento')
        

        print('agora escolha o qual esporte vôce quer fazer:')
        print('digite 1 para futsal na segunda feira\ndigite 2 para vôlei na terça \ndigite 3 para handebool na quarta feira\n' \
        'digite 4 para carimba na quinta feira\ndigite 5 para basquete na sexta feira')

        opção=int(input('escolha uma das opções.'))

        if opção==1:
            print('você escolheu jogar futsal na segunda feira')
        if opção==2:
            print('você escolheu jogar vôlei na terça feira')
        if opção==3:
            print('você escolheu jogar hamdebool na quarta feira')
        if opção==4:
            print('você escolheu jogar carimba na quinta feira')
        if opção==5:
            print('você escolheu jogar basquete na sexta feira')


def secretaria():
    fazer=int(input("oque você deseja fazer na secretaria:" \
    "\n1-pegar a agenda de sala" \
    "\n2-imprimir atividade" \
    "\n3- imprimir declaração"))


aluno()
secretaria()
