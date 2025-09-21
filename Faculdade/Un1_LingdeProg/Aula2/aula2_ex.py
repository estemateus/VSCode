# Máquina de venda automática de ingressos de cinema

# Solicita a idade do cliente
idade = int(input("Digite sua idade: "))

# Verifica a idade para sugestão de filme
if idade < 12:
    print("Recomendamos o filme infantil FILME 1.")
elif 12 <= idade < 18:
    print("Recomendamos o filme adolescente FILME 2.")
else:
    print("Recomendamos o filme emocionante FILME 3.")

# Verificação de ingressos disponíveis
quantidade_ingressos = 10 #Suponha que há 10 ingressos disponíveis

if quantidade_ingressos > 0:
    print("Ingressos disponíveis! Aproveite o filme!")
else:
    print("Desculpe, não há ingressos disponíveis no momento.")