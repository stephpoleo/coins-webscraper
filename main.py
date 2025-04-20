import requests

# Constants
url_coinbase = 'https://api.coinbase.com/v2/currencies'
url_wiki = 'https://en.wikipedia.org/wiki/List_of_circulating_currencies'

def get_coinbase_data():
    response = requests.get(url_coinbase)
    data = response.json()
    coinbase_list = []

    for currency in data['data']:
        coinbase_list.append({'id': currency['id'], 'name': currency['name']})

    return coinbase_list

def display_coinbase_size_and_list(coinbase_list):
    print("Lista de Coinbase:")
    print(coinbase_list)
    print(f"Tamaño de la lista de Coinbase: {len(coinbase_list)}\n")

if __name__ == "__main__":
    coinbase_data = get_coinbase_data()
    display_coinbase_size_and_list(coinbase_data)