import requests
from bs4 import BeautifulSoup
page = requests.get('https://trangvangvietnam.com/categories/99110/phan-bon-cac-dai-ly-phan-bon.html')
print(page)