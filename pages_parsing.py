from bs4 import BeautifulSoup
import requests
import pymongo



def get_links_from(channel, pages, who_sells = 0):
    list_view = '%s%s/pn%s' % (channel, who_sells, pages)
    web_response = requests.get(list_view)
    soup = BeautifulSoup(web_response.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t > a'):
            item_link = link.get('href').split('?')[0]
            print(item_link)

def get_item_info(url):
    web_response = requests.get(url)
    soup = BeautifulSoup(web_response.text, 'lxml')
    title = soup.select('div.box_left_top > h1.info_titile')[0].get_text()
    price = soup.select('span.price_now > i')[0].get_text()
    region = soup.select('div.palce_li > span > i')[0].get_text()
    tag = list(soup.select('div.quality')[0].stripped_strings)

    info = {'title':title, 'price':price, 'region':region, 'tag':tag}
    print(info)

#get_links_from('http://sz.58.com/shouji/', 1)
get_item_info('http://zhuanzhuan.58.com/detail/775672374084042754z.shtml')