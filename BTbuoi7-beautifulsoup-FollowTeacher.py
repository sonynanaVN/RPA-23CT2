from bs4 import BeautifulSoup
import requests

ULR="https://www.thegioididong.com/dtdd"
response = requests.get(ULR)
text = response.text
BeautifulSoup()