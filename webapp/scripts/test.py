import requests
from bs4 import BeautifulSoup

url = "https://www.zawya.com/en/economy/gcc/dubais-non-oil-businesses-expanded-in-january-but-at-a-slower-pace-due-to-red-sea-concerns-sztf8x0r"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup.prettify())

headline = soup.find('meta', {'property': 'og:title'})['content']
image_url = soup.find('meta', {'itemprop': 'thumbnailUrl'})['content']
description = soup.find('meta', {'itemprop': 'description'})['content']

print(f"Healdine: {headline}")
print(f"Image URL: {image_url}")
print(f"Description: {description}")
