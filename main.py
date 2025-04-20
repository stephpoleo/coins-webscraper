import requests

from bs4 import BeautifulSoup

# Constants
url_coinbase = 'https://api.coinbase.com/v2/currencies'
url_wiki = 'https://en.wikipedia.org/wiki/List_of_circulating_currencies'

def get_coinbase_data():
    response = requests.get(url_coinbase)
    data = response.json()
    coinbase_list = []

    for currency in data['data']:
        coinbase_list.append({'code': currency['id'], 'name': currency['name']})

    return coinbase_list

def display_base_size_and_list(list, list_name):
    print(f"Displaying list {list_name}:")
    print(list)
    print(f"List size: {len(list)}\n")

def display_sorted_list_by_code(list):
    sorted_list = sorted(list, key=lambda x: x['code'])
    print("Ordered list by code:")
    for currency in sorted_list:
        print(f"Code: {currency['code']}, Name: {currency['name']}")
    print(f"List size: {len(sorted_list)}\n")

def get_wiki_data():
    response = requests.get(url_wiki)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})
    rows = table.find_all('tr')

    wiki_list = []
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) > 0:
            currency_name = cols[len(cols)-5].text.split('[')[0].strip()
            currency_code = cols[len(cols)-3].text.split('[')[0].strip()
            if currency_code == '(none)':
                currency_code = 'N/A'
            wiki_list.append({'code': currency_code, 'name': currency_name})

    return wiki_list

def common_codes_list(wiki_list, coinbase_list):
    wiki_dict = {currency['code']: currency['name'] for currency in wiki_list}
    coinbase_dict = {currency['code']: currency['name'] for currency in coinbase_list}
    
    common_codes = set(wiki_dict.keys()).intersection(set(coinbase_dict.keys()))
    common_currencies = [] 
    
    for code in common_codes:
        if wiki_dict[code].upper() != coinbase_dict[code].upper():
            print(f"For code {code} the names do not match: {wiki_dict[code]} vs {coinbase_dict[code]}")
            common_currencies.append({
                'code': code,
                'name': F"{wiki_dict[code].upper()} or {coinbase_dict[code].upper()}"
            })
        else:
            common_currencies.append({
                'code': code,
                'name': wiki_dict[code].upper()
            })
    
    return common_currencies

if __name__ == "__main__":
    # Instruccion 1
    coinbase_data = get_coinbase_data()
    display_base_size_and_list(coinbase_data, "Coinbase Data")

    # Instruccion 2
    wiki_data = get_wiki_data()
    display_base_size_and_list(wiki_data, "Wiki Data")

    # Instruccion 3
    common_currencies = common_codes_list(wiki_data, coinbase_data)
    display_base_size_and_list(common_currencies, "Common Currencies, not sorted")

    # Instruccion 4
    display_sorted_list_by_code(common_currencies)