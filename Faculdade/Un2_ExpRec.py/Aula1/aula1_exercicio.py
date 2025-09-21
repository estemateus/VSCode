# Tupla de convidados
convidados = ("Alice", "Bob", "Carol", "David", "Eve")

# Lista de confirmações
confirmados = ["Bob", "David"]

# Identificar quem ainda não confirmou presença
nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir os  convidados que ainda não confirmaram presença
print("Convidados que ainda não confirmaram presença:")
for convidado in nao_confirmados:
    print(convidado)

# Enviar lembretes aos não confirmados
print("\nEnviando lembretes para os convidados que ainda não confirmaram presença...")