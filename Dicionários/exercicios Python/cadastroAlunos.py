import media 
import Situacao
def cadAlunos():
    nome = input("Insira o nome do Aluno: ")
    n1 = int(input("Digite a 1º Nota: "))
    n2 = int(input("Digite a 2º Nota: "))
    n3 = int(input("Digite a 3º Nota: "))
    med = media.media(n1,n2,n3)
    s = Situacao.situacao(med,nome)
    return ({
         "nome":nome,
         "n1": n1,
         "n2": n2,
         "n3": n3,
         "media": med,
         "Situação":s
        })
        
   
      
            