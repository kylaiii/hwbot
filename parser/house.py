import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

URL = "https://www.house.kg/kupit"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all("div", class_="listing")
    houses = []
    for item in items:
        houses.append({
         "title": item.find("p").getText(),
         "desc": item.find("div", class_='description').getText(),
         "address": item.find("div", class_='address').getText(),
         "price": item.find("div", class_='price').getText(),
         "price_in_soms":  item.find("div", class_='price-addition').getText(),
         "when": item.find("span").getText()
        })
    return houses

def parser():
    html = get_html(URL)
    get_data(html.text)
     if html.status_code == 200:
       answer=[]
       for page in range(1,3):
           html = get_html(f"{URL}?page={page}")
           current_page = get_data(html.text)
           answer.extend(current_page)
       return answer
    
     else:
         raise Exception("error in parser!")

parser()


