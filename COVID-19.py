Arquivo_internados = r'data\INTERNADOS.csv'
Arquivo_recuperados = r'data\RECUPERADOS.csv'
Arquivo_obitos = r'data\OBITOS.csv'
Arquivo_confirmados = r'data\CONFIRMADOS.csv'


def cidade(arqConf, nomeArq, a, b): #ALGORITMO DE PESQUISA POR CIDADE <-----------------------------
    cid = input("Digite o nome da cidade: ")
    totalConf = 0
    for linha in arqConf:
        valores = linha.split(';')
        if cid.upper() == valores[0] and valores[1] != '0': #OPERAÇÃO RELEVANTE <------------
            if nomeArq == Arquivo_internados or nomeArq == Arquivo_recuperados:
                totalConf = valores[1]
                data = valores[2]
            else:
                totalConf = int(valores[1]) + totalConf
                data = valores[2]
                
    print(cid.upper(), "teve um total de", totalConf, a, "até a data de", data,
          "\n\n(1) Detalhar\n(2) Voltar ao MENU")
    op = int(input("Opção:"))
    
    if op == 1:
        print('\n\n** Detalhamento de', a, 'por COVID-19 na cidade de', cid.upper(), '**\n')
        arqConf = open(nomeArq, 'r')
        for linha in arqConf:
            valores = linha.split(';')
            if cid.upper() == valores[0] and valores[1] != '0':
                print(valores[0], ':', valores[1], a,b,'data', valores[2])
            else:
                pass
    else:
        pass
    arqConf.close()
    

def shellSort(v): # ALGORITMO DE ORDENAÇÃO <------------------------------------------------------
    h = len(v) // 2  
    while h > 0:
        i = h
        while i < len(v):
            temp = v[i]
            trocou = False
            j = i - h
            while j >= 0 and v[j] > temp:
                v[j + h] = v[j]
                trocou = True
                j -= h

            if trocou:
                v[j + h] = temp
            i += 1
        h = h // 2


def regioes():
    print("\nDigite uma das mesoregioes diponiveis abaixo:\n"
"\nSUL\nLESTE\nNORTE\nCENTRO\nSUDESTE\nJEQUITINHONHA\nNORDESTE\nOESTE\nTRIANGULO DO SUL\n"
"CENTRO SUL\nLESTE DO SUL\nTRIANGULO DO NORTE\nNOROESTE\nVALE DO ACO\n")


def mesoreg(arqConf, arq,b):
    regioes()
    pesquisa = input("Pesquisar:")
    arqConf = open(arq, 'r')
    total=0
    for linha in arqConf:
        valores = linha.replace('\n',';').split(';')
        if pesquisa.upper() == valores[6] and valores[1] != '0':
            total = int(valores[1]) + total
            datas = valores[2]
    print('A mesoregiao',pesquisa.upper(), "teve um total de", total, b, datas,
                 "\n\n(1) Detalhar por data\n(2) Voltar ao MENU")
    op = int(input("Opção:"))
    if op == 1:
        data = input("\nBuscar data (DIA/MÊS/ANO): exemplo> 00/00/0000 <exemplo\nPesquisar: ")
        v=[]
        print('\n\n** Cidades que tiveram', b, 'confirmados no dia '+data+' por COVID-19 na mesoregiao de', pesquisa.upper(), '**\n')
        arqConf = open(arq, 'r')
        for linha in arqConf:
            valores = linha.replace('\n', ';').split(';')
            if pesquisa.upper() == valores[6] and valores[1] != '0':
                v.append([valores[0],valores[1],valores[2]])
        shellSort(v[2])
        for i in range(len(v)):
            if data == v[i][2]:
                print(v[i][0].upper(),":",v[i][1]+b)
    arqConf.close()


def imprimir(nomeArq,a):
    regioes()
    v=[]
    pesquisa = input("Pesquisar:")
    data = input("\nBuscar data (DIA/MÊS/ANO): exemplo> 00/00/0000 <exemplo\nPesquisar: ")
    arqRec = open(nomeArq,'r')
    for linha in arqRec:
        valores = linha.replace('\n', ';').split(';')
        if pesquisa.upper() == valores[6]:
            v.append([valores[0], valores[1], valores[2]])
    shellSort(v[2])
    for i in range(len(v)):
        if data == v[i][2]:
            print(v[i][0].upper(),":",v[i][1]+a)
    arqRec.close()

menu = 1
while menu > 0:
    print('\n* Toda pesquisa deve ser feita sem acento ou caracteres especiais *\nEscolha uma opção:\n(1) Confirmados\n(2) Internados\n(3) Recuperados\n(4) Obitos')
    menu = int(input("Opcao: "))

    #confirmados
    if menu == 1:
        arqConf = open(Arquivo_confirmados, 'r')
        opcConf = int(input(("\n(1)Pesquisar casos confirmados por cidade\n(2)Pesquisar casos confirmados por mesoregiao\n\nEscolha uma opção: ")))
        if opcConf == 1:
            cidade(arqConf, Arquivo_confirmados, 'caso(s) confirmados', 'na')
        elif opcConf == 2:
            mesoreg(arqConf, Arquivo_confirmados,' casos')

    # internados
    elif menu == 2:
        arqInte = open(Arquivo_internados, 'r')
        opcInte = int(input(("\n(1)Pesquisar internados por cidade\n(2)Mostrar internados por mesoregiao (ShellSort)\n\nEscolha uma opção: ")))
        if opcInte == 1:
            cidade(arqInte, Arquivo_internados, 'internado(s)', 'até a')
        elif opcInte == 2:
            imprimir(Arquivo_internados,' internados')

    # recuperados
    elif menu == 3:
        arqRec = open(Arquivo_recuperados, 'r')
        opcRec = int(input(("\n(1)Pesquisar casos recuperados por cidade\n(2)Mostrar casos recuperados por mesoregiao (ShellSort)\n\nEscolha uma opção: ")))
        if opcRec == 1:
            cidade(arqRec, Arquivo_recuperados, 'recuperado(s)', 'até a')
        elif opcRec == 2:
            imprimir(Arquivo_recuperados,' recuperados')

    # obitos
    elif menu == 4:
        arqObts = open(Arquivo_obitos, 'r')
        opcObt = int(input(("\n(1)Pesquisar obitos por cidade\n(2)Pesquisar óbitos por mesoregião\n\nEscolha uma opção: ")))
        if opcObt == 1:
            cidade(arqObts, Arquivo_obitos, 'obito(s) confirmados','na')
        elif opcObt == 2:
            mesoreg(arqObts, Arquivo_obitos, ' obito(s)')

