import requests
from bs4 import BeautifulSoup
URL = 'https://trangvangvietnam.com/categories/99110/phan-bon-cac-dai-ly-phan-bon.html'
page = requests.get(URL)
print(page)
