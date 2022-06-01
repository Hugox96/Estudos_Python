import cadastroAlunos

i = int(input("Insira a Quantidade de Alunos: "))

alunos={}

for x in range(i):
    alunos.update({x:cadastroAlunos.cadAlunos()})

    
p = input("Digite o Nome do Aluno para localizar: ")
for aluno in alunos:
    if p in aluno:
        print(aluno)
        