import os

# AINDA EM DESENVOLVIMENTO

def pausar():
    input('TECLE [ENTER] PARA CONTINUAR...')

def limpar_tela():
    os.system('cls')

def calcular_media():
    Notas_totais = []
    print('\n==== CALCULAR MINHA MÉDIA ====')
    qntd_avaliaçoes = int(input('QUANTIDADE DE AVALIAÇÕES ATÉ O MOMENTO: '))
    for i in range(qntd_avaliaçoes):
        notas = float(input(f'NOTA AVALIAÇÃO {i +1}: '))
        Notas_totais.append(notas)
    total_notas = sum(Notas_totais) / qntd_avaliaçoes
    maior_nota = max(Notas_totais)
    print('\n====================================================')
    print(f'SUA MÉDIA ATUALMENTE É DE {total_notas:.2f} PONTOS!')
    print(f'SUA MAIOR NOTA FOI DE: {maior_nota}')
    print('====================================================')
    return total_notas

def calcular_final():
    Notas_totais = []
    print('\n==== CALCULAR MINHA MÉDIA ====')
    qntd_unidades = int(input('QUANTIDADE DE UNIDADES: '))
    for i in range(qntd_unidades):
        notas = float(input(f'NOTA UNIDADE {i +1}: '))
        Notas_totais.append(notas)
    media_unidades = sum(Notas_totais) / qntd_unidades
    minimo = 15 - 2*media_unidades
    print('\n====================================================')
    print(f'SUA MÉDIA ATUALMENTE FOI DE {media_unidades:.2f} PONTOS!')
    print('====================================================')
    if media_unidades < 2.5:
        print('VOCÊ NÃO PODE FAZER A FINAL MÉDIA ABAIXO DO PERMITIDO!')
    else:
        print('VOCÊ PODE FAZER A FINAL')
        print(f'VOCÊ PRECISARÁ DE {minimo} PONTOS PARA SER APROVADO!')



#PROGRAMA PRINCIPAL
print('==============================================================================')
print('Bem vindo a Calculadora Acadêmica!')
print('Aqui você poderá calcular ou prever quanto será necessário para ser aprovado!')
print('==============================================================================')

while True:
    limpar_tela()
    print('====== CALCULADORA ACADÊMICA ========')
    print('[1] - CALCULAR MINHA MÉDIA TOTAL     ')
    print('[2] - QUANTO PRECISO P/ APROVAÇÃO?   ')
    print('[3] - QUANTO PRECISO NA FINAL?       ')
    print('=====================================\n')
    op = int(input('> '))
    if op == 1:
        calcular_media()
        pausar()

    elif op == 2:
        Notas_totais = []
        print('==== QUANTO PRECISO P/ APROVAÇÃO? ====')
        quant_unid = input('QUANTIDADES DE UNIDADES: ')
        media_aprov = input('MÉDIA PARA APROVAÇÃO: ')
        max_unid = quant_unid * 10
        qntd_avaliaçoes = int(input('QUANTIDADE DE AVALIAÇÕES ATÉ O MOMENTO: '))
        for i in range(qntd_avaliaçoes):
            notas = float(input(f'NOTA AVALIAÇÃO {i +1}: '))
            Notas_totais.append(notas)
        total_notas = sum(Notas_totais) 
        pausar()
    elif op == 3:
        print('==== QUANTO PRECISO NA FINAL? ====')
        calcular_final()
        pausar()

    else:
        print('OPÇÃO INVÁLIDA! DIGITE UMA OPÇÃO VÁLIDA! ')
        pausar()
    
