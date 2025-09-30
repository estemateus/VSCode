def analisador_numeros():
    numeros_pares = 0
    numeros_impares = 0

    while True:
        entrada = input("Digite um número inteiro ou sair para encerrar o programa: ")

        if entrada.lower() == 'sair':
            break
        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"O número {numero} é par")
                numeros_pares += 1 
            else:
                print(f"O número {numero} é impar")
                numeros_impares += 1
        except ValueError:
            print("Entrada inválida, por favor digite um número inteiro")
            continue
        print(f"\n Resultado")
        print(f"Total de números pares: {numeros_pares}")
        print(f"Total de números ímpares: {numeros_impares}")
analisador_numeros()