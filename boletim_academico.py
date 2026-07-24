import os
# ---------------------------------------------------------
# 🎓 Sistema Simples de Gestão Acadêmica 
# ---------------------------------------------------------

# Primeiro semestre
Materias = ['Lógica da Programação', 'Introdução a Computação', 'Introdução a Matemática', 'Inglês', 'Arquitetura da Computação']

# Número baseado na index das materias ////  Notas separadas por unidade dentro da lista
Notas_0 = [10]
Notas_1 = [9.2]
Notas_2 = [10,10]
Notas_3 = [7.4, 9]
Notas_4 = [7]

Unidades = [Notas_0, Notas_1, Notas_2, Notas_3, Notas_4]

# O sum() soma os números da lista e o len() conta quantas notas existem nela

media_0 = sum(Notas_0) / len(Notas_0)
media_1 = sum(Notas_1) / len(Notas_1)
media_2 = sum(Notas_2) / len(Notas_2)
media_3 = sum(Notas_3) / len(Notas_3)
media_4 = sum(Notas_4) / len(Notas_4)

# Criando a lista de médias finais exatamente na mesma ordem das matérias
media_por_materias = [media_0, media_1, media_2, media_3, media_4]
media_total = sum(media_por_materias) / len(Materias)
maior_nota = max(media_por_materias)
menor_nota = min(media_por_materias)
melhor_materia = Materias[media_por_materias.index(maior_nota)]
pior_materia = Materias[media_por_materias.index(menor_nota)]

def limpar_tela():
    os.system('cls')

#=============================================================================
limpar_tela()
print("-" * 40)
print("📊 BOLETIM DE DESEMPENHO - 1º SEMESTRE")
print("-" * 40)

# Um laço 'for' básico que passa pela posição (índice) de 0 até 4
for i in range(len(Materias)):
    print(f"Disciplina: {Materias[i]}")
    print(f'{len(Unidades[i])} Unidade(es) registrada(as) de 3 Unidades')
    print(f"Média Final: {media_por_materias[i]:.1f}")
    if media_por_materias[i] >= 7:
        print('Aprovado na disciplina!\n')
    else:
        print('Reprovado na discplina!\n')


print(f'MÉDIA GERAL DO 1º SEMESTRE: {media_total:.1f}')
print(f'A Maior média foi {maior_nota} na Materia {melhor_materia}. Parabéns!')
print(f'Materia que exige atenção é {pior_materia} com a média {menor_nota}')
print("-" * 40)
