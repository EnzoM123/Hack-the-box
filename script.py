import requests
from bs4 import BeautifulSoup
url = 'http://46.101.47.107:32497'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
teste1 = soup.find_all('input')[0].get_text('Oi')
print(teste1)