import requests

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()[moeda + "BRL"]  # Corrigido aqui
    return f"Moeda: {moeda}/BRL\n Valor: R${dados['high']}\n Mínimo: R${dados['low']}\n Atualização: {dados['create_date']}"

moeda = input("Digite o código (USD, EUR): ")
print(obter_cotacao(moeda))