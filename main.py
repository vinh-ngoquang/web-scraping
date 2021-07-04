import pry
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://trangvangvietnam.com/categories/99160/phan-bon-cong-ty-phan-bon-san-xuat-va-ban-buon.html'


def execute():
    page = requests.get(BASE_URL)
    result = BeautifulSoup(page.content, "html.parser")
    max_page = get_max_page_num(result)
    for page_num in range(1, max_page + 1):
        result_arr = scraping_in_page(page_num)
        pry()


def cast_to_number(str):
    return int(str) if str.isdigit() else -1


def get_max_page_num(soup_result):
    pagers = soup_result.find(id="paging").find_all("a")
    text_num_pages = map(lambda a_tag: a_tag.get_text(), pagers)
    num_pages = map(lambda text_page: cast_to_number(
        text_page), text_num_pages)
    return max(num_pages)


def scraping_in_page(page_num):
    url = BASE_URL + '?page=' + str(page_num)
    page = requests.get(url)
    result = BeautifulSoup(page.content, "html.parser")
    companies = result.find_all("div", class_="boxlistings")

    arr = []
    for company in companies:
        name = company.find(class_="company_name").get_text()
        # print(name)
        phone = company.find(class_="thoaisection").get_text()
        # print(phone)
        email_raw = company.find(class_="email_text")
        if email_raw != None:
            email = email_raw.find("a")['title']
        else:
            email = ''
        print(email)
        website_raw = company.find(class_="website_text")
        if website_raw != None:
            website = print(website_raw.find("a")['href'])
        else:
            website = ''
        address = company.find_all(class_="diachisection")[1].get_text()

        # TODO: Append, not flatten
        arr += [name, phone, email, website, address]

    return arr


execute()
