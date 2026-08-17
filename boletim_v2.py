import os

Notas = {
    'LOGICA DE PROGRAMAÇÃO':  [10,5.5,9],
    'INTRODUCAO A MATEMATICA': [10,10],
    'INTRODUCAO A COMPUTACAO' : [9.2],
    'ARQUITETURA DE COMPUTADORES': [7,9.2],
    'INGLES': [7.4,9]
}

def limpar_tela():
    os.system('cls')

def pausar():
    input('[ENTER] para continuar....')

def pular_linha():
    print('\n')

def verificar_aprovacao():
        print('aprovado')

def ver_boletim_completo(dicionario):
    for materias, lista in dicionario.items():
        media = sum(lista) / len(lista)
        print(f" MAT: {materias} - Notas: {lista} - Média: {media:.2f}")

def pesquisar_materias(pesquisada):
    encontrou = False
    for materias in Notas:
        if pesquisada in materias:
            print(f' {materias} - NOTAS: {Notas[pesquisada]} ')
            encontrou = True
            return materias
        
    if not encontrou:
        print(' MÁTERIA NÃO ENCONTRADA!')

#MENU PRINCIPAL

while True:
    limpar_tela()
    print('          BOLETIM ÂCADEMICO        ')
    print(' [1] - VER MEU BOLETIM COMPLETO    ')
    print(' [2] - VER POR SEMESTRES           ')
    print(' [3] - PESQUISAR MATÉRIAS          ')
    print(' [0] - SAIR                        ')
    pular_linha()
    op = input('>: ')
    if op == '1':
        limpar_tela()        
        print('       BOLETIM COMPLETO        ')
        pular_linha()
        ver_boletim_completo(Notas)
        pular_linha()
        pausar()
    elif op =='2':
        print('')
    elif op =='3':
        limpar_tela()
        print('  PESQUISAR MATERIAS \n')
        pesquisada = input(' Máteria para pesquisa: > ').upper().strip()
        pesquisar_materias(pesquisada)
        pular_linha()
        pausar()

    elif op =='0':
        print('')
        break
    else: 
        print('OPÇÃO INVÁLIDA!')