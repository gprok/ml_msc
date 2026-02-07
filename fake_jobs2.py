import requests
from bs4 import BeautifulSoup 

response = requests.get('https://realpython.github.io/fake-jobs/')

print(response.text)

soup = BeautifulSoup(response.text, "html.parser")