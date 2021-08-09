while True:
    id_usuario = 0
    id_usuario += 1
    arq = open("registros.txt", "a")
    print("Bem vindo onde começa")
    register_usuario = input("Registre seu login: ")
    register_senha = input("Registre seua senha: ")
    

    arq.writelines(f"-------------- Usuario {id_usuario} ---------------\n")
    arq.writelines(f"Nome de usuario: {register_usuario}\n") #Aqui ele vai escrever no markdown ou bloco de notas
    arq.writelines(f"Senha do usuario: {register_senha}\n") # o nome e senha do usuario.
    arq.writelines("-----------------------------------------\n")
    
    print("registrou com sucesso!")
    
    arq.close()

    arq = open("registros.txt")

    print("Bem vindo faça seu login")
    login_usuario = input("Digite seu login: ")
    login_senha = input("Digite sua senha: ")
    
    ler_nome = arq.readlines()
    ler_senha = arq.readlines()
    
    def verificar_nome_senha(login_usuario, ler_nome, login_senha, ler_senha):
        if (("Nome de usuario: {login_usuario}\n") in ler_nome):
            if ("Senha do usuario: {login_senha}\n" in ler_senha):
                print("você logou com sucesso!")
            else:
                print("Você digitou senha errado!")
        else:
            print("você digitou seu usuario errado")
    arq.close()

    verificar_nome_senha(login_usuario, ler_nome, login_senha, ler_senha)

    parar = 'n'
    parar = input("deseja continuar? S//N:\n")
    if parar != 's':
        break
