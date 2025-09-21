# range(5) cria uma sequência que se inicia em 0 e vai até 4, realizando 5 iterações.
for x in range (5):
    print(x)

# range(2, 7) cria uma sequência que se inicia em 2 e vai até 6, realizando 5 iterações.
for y in range (2, 7):
    print(y)

# range(1, 11, 2) cria uma sequência que começa em 1, vai até 10 e incrementa de 2 em 2.
for z in range (1, 11, 2):
    print(z)

# O comando “break” é usado para interromper a execução de uma estrutura de repetição quando uma determinada condição é atendida.
for numero in range (1, 11):
    if numero % 2 == 0:
        print(f"O primeiro número par é: {numero}")
        break

# O comando “continue” é usado para pular a iteração atual em uma estrutura de repetição e continuar com a próxima iteração.
for numero in range (1, 11):
    if numero == 5:
        continue
    print(numero)