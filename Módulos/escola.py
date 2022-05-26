#Criando o arquivo para ler a função alunos

# Importante o arquivo com a função que retornar a lista dos alunos
import alunos
# Criando uma variável para salvar a quantidade de alunos
Total_Alunos = 2

lista_alunos = []
for i in range(Total_Alunos):
    lista_alunos.append (alunos.alunos_info())
print(lista_alunos)    

