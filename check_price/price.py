from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import facebook



def check_price():

    url='https://deals.souq.com/eg-en/smart-tvs/c/15236'


    url_req=Request(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'})
    url_req = urlopen(url_req).read()
    page_soup=bs(url_req,"html.parser")
    containers=page_soup.findAll("div",{"class":"column column-block block-grid-large"})

    brand = [container.div.div.div.a["data-title"][0:20]
             for container in containers]

    price = [container.findAll("span", {"class": "sk-clr1"})[0].text.replace('EGP', '').replace(',', '').strip()
             for container in containers]


    msg = {brand[index]: price[index] for index in range(len(brand))}
    return str(msg)


def post_on_FB(msg):

    token = ''

    fb = facebook.GraphAPI(access_token=token)
    fb.put_object(parent_object='me', connection_name='feed', message=msg)


msg=check_price()
post_on_FB(msg)