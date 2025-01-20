import requests

#Salvando o link do produto que quero pesquisar
url = "https://www.mercadolivre.com.br/samsung-galaxy-s24-ultra-5g-dual-sim-256-gb-titnio-cinza-12-gb-ram/p/MLB34491099#polycard_client=search-nordic&searchVariation=MLB34491099&wid=MLB4392480274&position=2&search_layout=stack&type=product&tracking_id=50145180-47c1-4ece-855f-ba5c3f8a221b&sid=search"
response = requests.get(url)
print(response)