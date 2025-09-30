import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    return f"Cep: {dados['cep']}\nRua: {dados['logradouro']}\nBairro: {dados['bairro']}\nCidade: {dados['localidade']}\nEstado: {['UF']}"

cep = input("Digite o CEP: ")
print(consultar_cep(cep))