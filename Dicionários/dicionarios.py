"""O dicionário Python é uma coleção não ordenada de itens. Cada item de um dicionário tem um par chave/valor.
Os dicionários são otimizados para recuperar valores quando a chave é conhecida. """

#Criar um dicionário é simples, só precisa usar {} com chaves e valores:
meu_dicionario = {"Nome":"Hugo", "Idade":"26", "Cidade": "Rio de Janeiro"}
print(meu_dicionario) 

#Acessando um item no dicionário, no caso o valor Hugo com a chave Nome
valor = meu_dicionario["Nome"]
print(valor)

#Adicionando novos valores no dicionário:
meu_dicionario["email"] = "hugoalves@gmail.com"
print(meu_dicionario)

#Verificando se os valores estão no dicionário
if "Idade" in meu_dicionario:
    print("Idade está no dicionário")
else:
    print("Não está") 

#Loops no dicionário para percorrer as chaves e os valores no dicionário
for key, value in meu_dicionario.items():
    print(key,value) 

#Percorrendo as chaves
for key in meu_dicionario.keys():
    print(key)
#Percorrendo os valores
for value in meu_dicionario.values():
    print(value)              
