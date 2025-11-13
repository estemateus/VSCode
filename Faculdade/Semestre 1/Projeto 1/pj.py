# CLÍNICA VIDA+: Estrutura Principal e Menu
# Objetivo: Montar o esqueleto do programa e o loop de navegação.

# ====================================================================

# O dicionário base
pacientes = []

def exibir_menu():
    #Esta função é responsável apenas por mostrar as opções do sistema.
    print("\n" + "=" * 25 + " BEM-VINDO AO SISTEMA CLÍNICA VIDA+ " + "=" * 25) # Cabeçalho
    print("O que você deseja fazer hoje?")
    print("1. Cadastrar novo paciente")
    print("2. Ver estatísticas da clínica")
    print("3. Buscar paciente pelo nome")
    print("4. Listar todos os pacientes")
    print("5. Sair do Sistema")
    print("=" * 75)

# Lista de funções referentes a cada opção da função principal:
def cadastrar_paciente(lista_pacientes):
                    print("=" * 30 + " NOVO CADASTRO " + "=" * 30)
                    # Solicita os dados do paciente e o adiciona à lista.
                    nome = input("Nome do paciente: ").strip().title()
                    telefone = input("Telefone: ").strip()
                    # Reutilizando tratamento de erros (Evitando problemas com a idade)
                    while True:
                        try:
                            idade_str = input("Idade: ").strip()
                            idade = int(idade_str)
                            if idade <= 0:
                                print("[ERRO] Idade inválida. Por favor, digite a idade usando apenas números.")
                                continue
                            break
                        except ValueError:
                            print("[ERRO] Idade inválida. Por favor, digite a idade usando apenas números.")
                    # Armazenando os dados em um dicionário
                    novo_paciente = {
                        'nome': nome,
                        'idade': idade,
                        'telefone': telefone
                    }
                    # Adicionando o dicionário à lista principal de pacientes
                    lista_pacientes.append(novo_paciente)
                    # Finalizando a lógica
                    print("\nPaciente cadastrado com sucesso!")

def listar_pacientes(lista_pacientes):
    # Exibindo todos os pacientes cadastrados na lista de forma organizada.
    print("=" * 28 + " LISTA DE PACIENTES " + "=" * 28)
    
    # Verificando se há pacientes cadastrados antes de tentar listar
    if not lista_pacientes: # Checa se a lista está vazia
        print("\nNenhum paciente cadastrado ainda.")
        
    else:
        # Usando um loop 'for' para percorrer a lista
        for i, paciente in enumerate(lista_pacientes):
            # i é o índice (para numerar), e paciente é o dicionário
            
            # Exibe o número do paciente e seus dados de forma organizada
            print(f"\n= Paciente {i + 1} =")
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']} anos")
            print(f"Telefone: {paciente['telefone']}")
            
    print("=" * 75)

# FUNÇÃO PRINCIPAL DO PROGRAMA
def main():
    while True:  # Rodando o programa em ciclo contínuo, esperando a ação do usuário.
        exibir_menu()
        try: # Usamos o 'try-except' para tratamento erros.
            # Implementar o menu simples para navegação
            opcao = int(input("Escolha a opção desejada: "))

            if opcao == 1:
                cadastrar_paciente(pacientes) # LÓGICA DO CADASTRO
                pass

            elif opcao == 2:
                # LÓGICA DAS ESTATÍSTICAS
                pass

            elif opcao == 3:
                # LÓGICA DA BUSCA
                pass

            elif opcao == 4:
                listar_pacientes(pacientes) # LÓGICA DA LISTAGEM
                pass

            elif opcao == 5:
                print("\nEncerrando o Sistema VIDA+. Tenha um bom dia!")
                break  # O 'break' encerra o loop 'while True', e o programa termina.

            else:
                # Se o número digitado não for de 1 a 5
                print("\n[ATENÇÃO] Opção inválida! Por favor, escolha um número DE 1 a 5.")

        except ValueError:
            # Captura o erro caso o usuário digite algo que não seja um número
            print("\n[ERRO] Por favor, digite apenas números para selecionar uma opção.")


# Garantindo que o programa comece a rodar pela função 'main()' quando o arquivo for executado.
if __name__ == "__main__":
    main()