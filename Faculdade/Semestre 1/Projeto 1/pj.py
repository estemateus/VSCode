# ====================================================================
# Passo 2: Estrutura Principal e Menu - CLÍNICA VIDA+
# Objetivo: Montar o esqueleto do programa e o loop de navegação.
# ====================================================================

# === A LISTA QUE VAI GUARDAR TUDO (Checklist: Implementar a lista e dicionários) ===
# 'pacientes' é a nossa base de dados. Ela é uma lista, e dentro dela,
# cada paciente será um dicionário (chave: valor, como 'nome': 'João').
pacientes = []

def exibir_menu():
    """Esta função é responsável apenas por mostrar as opções do sistema."""
    # (Checklist: Exibir o cabeçalho)
    print("\n" + "=" * 25 + " BEM-VINDO AO SISTEMA CLÍNICA VIDA+ " + "=" * 25)
    print("O que você deseja fazer hoje?")
    print("1. Cadastrar novo paciente")
    print("2. Ver estatísticas da clínica")
    print("3. Buscar paciente pelo nome")
    print("4. Listar todos os pacientes")
    print("5. Sair do Sistema")
    print("=" * 75)

# === O CORAÇÃO DO PROGRAMA (Checklist: Implementar o loop principal) ===
def main():
    """É aqui que o programa roda em um ciclo contínuo, esperando a ação do usuário."""
    while True:
        exibir_menu()

        # Usamos o 'try-except' para tratar erros, como o usuário digitar texto em vez de um número.
        # Isso atende ao requisito de 'Tratamento de Erros' e evita que o programa quebre!
        try:
            # (Checklist: Implementar o menu simples para navegação)
            opcao = int(input("Escolha a opção desejada: "))

            if opcao == 1:
                print("\n[AÇÃO] Preparando para cadastrar um novo paciente...")
                # LÓGICA DO CADASTRO ENTRA AQUI
                pass

            elif opcao == 2:
                print("\n[AÇÃO] Calculando as estatísticas da clínica...")
                # LÓGICA DAS ESTATÍSTICAS ENTRA AQUI
                pass

            elif opcao == 3:
                print("\n[AÇÃO] Iniciando a busca por paciente...")
                # LÓGICA DA BUSCA ENTRA AQUI
                pass

            elif opcao == 4:
                print("\n[AÇÃO] Exibindo todos os pacientes cadastrados...")
                # LÓGICA DA LISTAGEM ENTRA AQUI
                pass

            elif opcao == 5:
                print("\nEncerrando o Sistema VIDA+. Tenha um bom dia!")
                break  # O 'break' encerra o loop 'while True', e o programa termina.

            else:
                # Se o número digitado não for de 1 a 5
                print("\n[ATENÇÃO] Opção inválida! Por favor, escolha um número válido do menu.")

        except ValueError:
            # Captura o erro caso o usuário digite algo que não seja um número (como 'a' ou 'menu')
            print("\n[ERRO] Por favor, digite apenas números para selecionar uma opção.")


# Garante que o programa comece a rodar pela função 'main()' quando o arquivo for executado.
if __name__ == "__main__":
    main()