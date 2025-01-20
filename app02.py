import requests
from bs4 import BeautifulSoup

#Criando uma função que recebe a url e retorna o texto completo da página
def fetch_page():
    url = "https://www.mercadolivre.com.br/samsung-galaxy-s24-ultra-5g-dual-sim-256-gb-titnio-cinza-12-gb-ram/p/MLB34491099#polycard_client=search-nordic&searchVariation=MLB34491099&wid=MLB4392480274&position=2&search_layout=stack&type=product&tracking_id=50145180-47c1-4ece-855f-ba5c3f8a221b&sid=search"
    response = requests.get(url)
    return response.text

#Recebe o html da página e trata pegando elementos pela classe
def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    product_name = soup.find('h1', class_='ui-pdp-title').get_text()
    prices = soup.find_all('span', class_='andes-money-amount__fraction')
    old_price: int = int(prices[0].get_text().replace('.', ''))
    new_price: int = int(prices[1].get_text().replace('.', ''))
    installment_price: int = int(prices[2].get_text().replace('.', ''))
    
    return {
        'product_name': product_name,
        'old_price': old_price,
        'new_price': new_price,
        'installment_price': installment_price
    }
    print(product_name)
    print(old_price, new_price, installment_price)

if __name__ == "__main__":
    page_content = fetch_page()
    produto_info = parse_page(page_content)
    print(produto_info)