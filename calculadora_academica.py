import os

# AINDA EM DESENVOLVIMENTO

def pausar():
    input('TECLE [ENTER] PARA CONTINUAR...')

def limpar_tela():
    os.system('cls')


print('==============================================================================')
print('Bem vindo a Calculadora Acadêmica!')
print('Aqui você poderá calcular ou prever quanto será necessário para ser aprovado!')
print('==============================================================================')

while True:
    limpar_tela()
    print('====== CALCULADORA ACADÊMICA ========')
    print('[1] - CALCULAR MINHA MÉDIA TOTAL     ')
    print('[2] - QUANTO PRECISO P/ APROVAÇÃO?   ')
    print('=====================================\n')
    op = int(input('> '))
    if op == 1:
        Notas_totais = []
        print('==== CALCULAR MINHA MÉDIA ====')
        qntd_avaliaçoes = int(input('QUANTIDADE DE AVALIAÇÕES ATÉ O MOMENTO: '))
        for i in range(qntd_avaliaçoes):
            notas = float(input(f'NOTA AVALIAÇÃO {i +1}: '))
            Notas_totais.append(notas)
        total_notas = sum(Notas_totais) / qntd_avaliaçoes
        maior_nota = max(Notas_totais)
        print(f'SUA MÉDIA ATUALMENTE É DE {total_notas} PONTOS!')
        print(f'SUA MAIOR NOTA FOI DE: {maior_nota}')



        pausar()
    elif op == 2:
        print('==== QUANTO PRECISO P/ APROVAÇÃO? ====')
        pausar()
    else:
        print('OPÇÃO INVÁLIDA! DIGITE UMA OPÇÃO VÁLIDA! ')
        pausar()
    
