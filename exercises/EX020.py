import random 

primeiro_aluno = input("Primeiro aluno: ")
segundo_aluno = input("Segundo aluno: ")
terceiro_aluno = input("Terceiro aluno: ")
quarto_aluno = input("Quarto aluno: ")

lista_alunos = (primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno)

k = 4
#ordem_alunos_escolhidos = (random.sample(lista_alunos))

print(f"A ordem de alunos escolhida é {random.sample(lista_alunos, k)}")
