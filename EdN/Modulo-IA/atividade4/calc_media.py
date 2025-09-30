def registrar_notas():
    notas = []
    while True:
        try:
            entrada = input("Digite a nota do aluno para continuar ou fim para encerrar: ")
            if entrada.lower() == 'fim':
                break
            nota = float(entrada)

            if nota >= 0 and nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, digite uma nota de 0 a 10 para continuar ou fim para encerrar")
    
    if notas:
        media = sum(notas) / len(notas)
        print(f"A media da turma: {media:.2f}")
        print(f"Total de notas validas registradas: {len(notas)}")

registrar_notas()