import os
def limpar_tela():
    os.system('cls')

def pausar():
    os.system('pause')
def pular_linha():
    print('\n')

def genesis_1(capitulo):
    if capitulo == 1:
        limpar_tela()
        print('==== GÊNESIS CAPÍTULO 1 ====')
        print('1: No princípio, Deus criou os céus e a terra.')
        print('2: A terra era sem forma e vazia; havia trevas sobre a face do abismo, e o Espírito de Deus pairava sobre as águas.')
        print('3: Disse Deus: "Haja luz", e houve luz.')
        print('4: Deus viu que a luz era boa, e separou a luz das trevas.')
        print('5: Deus chamou à luz "dia", e às trevas chamou "noite". Houve tarde e manhã, o primeiro dia.')
        print('6: Disse Deus: "Haja um firmamento no meio das águas, e separação entre águas e águas."')
        print('7: Deus fez o firmamento e separou as águas que estavam debaixo do firmamento das águas que estavam por cima do firmamento. E assim foi.')
        print('8: Deus chamou ao firmamento "céus". Houve tarde e manhã, o segundo dia.')


def transferir(op, capitulo):
    if op == 1 and capitulo == 1:
        genesis_1(1)
        pausar()

Antigo_Testamento = [['Gênesis', 50], ['Êxodo', 40], ['Levítico', 27], ['Números', 36], ['Deuteronômio', 34], ['Josué', 24], ['Juízes', 21], ['Rute', 4], ['1 Samuel', 31], ['2 Samuel', 24], ['1 Reis', 22], ['2 Reis', 25], ['1 Crônicas', 29], ['2 Crônicas', 36], ['Esdras', 10], ['Neemias', 13], ['Ester', 10], ['Jó', 42], ['Salmos', 150], ['Provérbios', 31], ['Eclesiastes', 12], ['Cânticos', 8], ['Isaías', 66], ['Jeremias', 52], ['Lamentações', 5], ['Ezequiel', 48], ['Daniel', 12], ['Oséias', 14], ['Joel', 3], ['Amós', 9], ['Obadias', 1], ['Jonas', 4], ['Miquéias', 7], ['Naum', 3], ['Habacuque', 3], ['Sofonias', 3], ['Ageu', 2], ['Zacarias', 14], ['Malaquias', 4]]
Novo_Testamento = [['Mateus', 28], ['Marcos', 16], ['Lucas', 24], ['João', 21], ['Atos dos Apóstolos', 28], ['Romanos', 16], ['1 Coríntios', 16], ['2 Coríntios', 13], ['Gálatas', 6], ['Efésios', 6], ['Filipenses', 4], ['Colossenses', 4], ['1 Tessalonicenses', 5], ['2 Tessalonicenses', 3], ['1 Timóteo', 6], ['2 Timóteo', 4], ['Tito', 3], ['Filemom', 1], ['Hebreus', 13], ['Tiago', 5], ['1 Pedro', 5], ['2 Pedro', 3], ['1 João', 5], ['2 João', 1], ['3 João', 1], ['Judas', 1], ['Apocalipse', 22]]
#INDICIE DE LIVROS DA BÍBLIA 
# 0 REPRESENTA O NOME DO LIVRO E 1 REPRESENTA A QUANTIDADE DE CAPÍTULOS DO LIVRO

while True:
    limpar_tela()
    print('==================== BÍBLIA SAGRADA ====================')
    print('[1] - ANTIGO TESTAMENTO')  
    print('[2] - NOVO TESTAMENTO')
    print('[0] - SAIR')
    print('=========================================================')
    op = int(input('> '))
    if op == 1:
        limpar_tela()
        print('==================== ANTIGO TESTAMENTO ====================')
        for i in range(len(Antigo_Testamento)):
            print(f'[{i + 1}] - {Antigo_Testamento[i][0]} - {Antigo_Testamento[i][1]} CAPÍTULOS')
        print('=========================================================')
        livro = int(input('QUAL LIVRO DESEJA CONSULTAR? '))
        if livro >= 1 and livro <= len(Antigo_Testamento):
            capitulo = int(input(f'QUAL CAPÍTULO DESEJA CONSULTAR EM {Antigo_Testamento[livro - 1][0]}? '))
            if 1 <= capitulo <= Antigo_Testamento[livro - 1][1]:
                print(f'VOCÊ CONSULTOU O LIVRO DE {Antigo_Testamento[livro - 1][0]}, CAPÍTULO {capitulo}.')
                transferir(livro, capitulo)
            else:
                print('CAPÍTULO INVÁLIDO! TENTE NOVAMENTE!')
                pausar()
    elif op == 2:
        limpar_tela()
        print('==================== NOVO TESTAMENTO ====================')
        for i in range(len(Novo_Testamento)):
            print(f'[{i + 1}] - {Novo_Testamento[i][0]} - {Novo_Testamento[i][1]} CAPÍTULOS')
        print('=========================================================')
        livro = int(input('QUAL LIVRO DESEJA CONSULTAR? '))
        if livro >= 1 and livro <= len(Novo_Testamento):
            capitulo = int(input(f'QUAL CAPÍTULO DESEJA CONSULTAR EM {Novo_Testamento[livro - 1][0]}? : > '))
            if 1 <= capitulo <= Novo_Testamento[livro - 1][1]:
                print(f'VOCÊ CONSULTOU O LIVRO DE {Novo_Testamento[livro - 1][0]}, CAPÍTULO {capitulo}.')
                transferir(livro, capitulo)
            else:
                print('CAPÍTULO INVÁLIDO! TENTE NOVAMENTE!')
                pausar()
    elif op == 0:
        print('SAINDO DO PROGRAMA...')
        pausar()
        break
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
        pausar()