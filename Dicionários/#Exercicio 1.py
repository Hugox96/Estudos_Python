# Exercicio 1

"""No dicionário abaixo, temos os dados de acesso de 4 usuários, cada um com seu login e senha, onde o login é a chave e a senha o valor.
Faça um script que peça ao usuário seu login e senha, se tiver certo envie uma mensagem de acesso autorizado, 
se fornecer a senha errada, informe o erro"""

# 1º Precisamos criar o dicionário com 4 chaves e valores
# 2º Avalar os inputs
# 3º Depois avaliar com um if se os valores estão corretos

"---------------- Declarando os dicionários ----------------- "

# login_senha ={'Lucas:': "Onepiece", "Hugo:": "Flamengo", "Iris": "Unhas", "Adonai": "Berserk"}
# print(login_senha)

# "---------------- Avaliando os inputs ----------------- "
# login = input("Digite seu login: ")
# senha = input("Digite sua senha: ")

# if login_senha[login] == senha:
#     print("Autorizado")
# else:
#     print("Usuário não cadastrado")


loginSenha={'joao'   : 'rush',
            'maria'  : 'yes',
            'zezinho': 'genesis'}

login=input("Qual seu login: ")
senha=input("Senha: ")

if loginSenha[login] == senha:
    print("Acesso autorizado...")
else:
    print("Senha errada")


