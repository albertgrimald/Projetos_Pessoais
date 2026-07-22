import os

def pausar():
    input('TECLE [ENTER] PARA CONTINUAR...')

def limpar_tela():
    os.system('cls')

def calcular_media(max,qnt,notas):
    media = (max * qnt) / notas
    return media



print('==============================================================================')
print('Bem vindo a Calculadora Acadêmica!')
print('Aqui você poderá calcular ou prever quanto será necessário para ser aprovado!')
print('==============================================================================')

while True:
    limpar_tela()
    print('====== CALCULADORA ACADÊMICA ========')
    print('[1] - CALCULAR MINHA MÉDIA           ')
    print('[2] - QUANTO PRECISO P/ APROVAÇÃO?   ')
    print('=====================================\n')
    op = int(input('> '))
    if op == 1:
        Notas_totais = []
        nota_max = 0
        print('==== CALCULAR MINHA MÉDIA ====')
        nota_max = int(input('NOTA MÁXIMA DA UNIDADE: '))
        quant_aval = int(input('QNTD DE AVALIAÇÕES FEITAS: '))
        for i in range(quant_aval):
            notas = float(input(f'NOTA {i +1}: '))
            Notas_totais.append(notas)
        calcular_media(nota_max,quant_aval, sum(Notas_totais))
        print(calcular_media(nota_max,quant_aval, sum(Notas_totais)))

        pausar()
    elif op == 2:
        print('==== QUANTO PRECISO P/ APROVAÇÃO? ====')
        pausar()
    else:
        print('OPÇÃO INVÁLIDA! DIGITE UMA OPÇÃO VÁLIDA! ')
        pausar()
    
