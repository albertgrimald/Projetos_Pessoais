import os
def limpar_tela():
    os.system('cls')

def pausar():
    os.system('pause')

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
    elif op == 2:
        limpar_tela()
        print('==================== NOVO TESTAMENTO ====================')
        for i in range(len(Novo_Testamento)):
            print(f'[{i + 1}] - {Novo_Testamento[i][0]} - {Novo_Testamento[i][1]} CAPÍTULOS')
        print('=========================================================')
        livro = int(input('QUAL LIVRO DESEJA CONSULTAR? '))
    elif op == 0:
        print('SAINDO DO PROGRAMA...')
        pausar()
        break
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
        pausar()