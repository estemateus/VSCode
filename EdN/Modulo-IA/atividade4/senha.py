def verifica_senha():
    while True:
        senha = input("Digite uma senha ou 'sair' para encerrar o programa: ")

        if senha.lower() == 'sair':
            print("Programa encerrado!")
            break

        if len(senha) < 8:
            print("Por questões de segurança, digite uma senha com no mínimo 8 caracteres")
            continue

        if not any(letra.isdigit() for letra in senha):
            print("Por questões de segurança sua senha deve conter pelo menos um número")
            continue
        
        print("Senha forte de válida")
        break

verifica_senha()