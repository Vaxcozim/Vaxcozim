print("Me Informe A Senha Correta!")
senha=123
while True:
    senha = int(input("Digite a senha: "))
    if senha == 123:
        print("Senha Correta!")
        break
    if senha != 123:
        print("Senha Incorreta, Digite Novamente!")
        continue