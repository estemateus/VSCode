# Definindo uma função chamada "par"
def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
# Testando a função
numero = 123120
if par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

# Testando a função com outro número
numero = 1355989
if par(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")