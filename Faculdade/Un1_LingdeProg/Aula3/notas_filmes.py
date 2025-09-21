filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

print()
print()
print()

for filme in filmes:
    while True:
        classificacao = input(f"{filme} de 1 a 5 (ou 0 para sair): ")
        if classificacao == "0":
            print(f"{filme} Interrompida")
            break # Encerra o loop interno com "break"
        classificacao = int(classificacao)
        if classificacao < 1 or classificacao > 5:
            print("Classificação inválida.")
        else:
            print(f"{filme} classificado com {classificacao} estrelas.\n")
            break # Sai do loop interno e passa para o próximo filme
print()