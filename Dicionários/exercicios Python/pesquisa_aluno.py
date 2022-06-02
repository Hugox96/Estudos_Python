
def procurar_alunos(aluno,pesquisa):
    for i in aluno:
        chave = aluno[i]
        if chave["nome"] == pesquisa:
            print("Aluno encontrado ")