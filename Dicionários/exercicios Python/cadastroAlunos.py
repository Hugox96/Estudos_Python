import media 
import situacao
import observacao
def cadAlunos():
    nome = input("Insira o nome do Aluno: ")
    n1 = int(input("Digite a 1º Nota: "))
    n2 = int(input("Digite a 2º Nota: "))
    n3 = int(input("Digite a 3º Nota: "))
    med = media.media(n1,n2,n3)
    situacao_aluno = situacao.situacao_func(med,nome)
    obs = observacao.obs_aluno()
    return ({
         "nome":nome,
         "n1": n1,
         "n2": n2,
         "n3": n3,
         "media": med,
         "Situação":situacao_aluno,
         "Observaçao":obs
        })
        
   
      
            