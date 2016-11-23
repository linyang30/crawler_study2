from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_info = ceshi['item_info']


def get_links_from(channel, pages, who_sells = 0):
    list_view = '%s%s/pn%s' % (channel, who_sells, pages)
    web_response = requests.get(list_view)
    soup = BeautifulSoup(web_response.text, 'lxml')
    if soup.find('td', 't'):
        for link in soup.select('td.t > a'):
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            print(item_link)

def get_item_info(url):
    web_response = requests.get(url)
    soup = BeautifulSoup(web_response.text, 'lxml')
    no_longer_exist = soup.select('div.button_li > span.soldout_btn') if soup.find('span', 'soldout_btn') else True
    if no_longer_exist:
        title = soup.select('div.box_left_top > h1.info_titile')[0].get_text() if soup.find('h1', 'info_titile') else None
        price = soup.select('span.price_now > i')[0].get_text() if soup.find('span', 'price_now') else None
        region = soup.select('div.palce_li > span > i')[0].get_text() if soup.find('div', 'palce_li') else None
        tag = list(soup.select('div.quality')[0].stripped_strings) if soup.find('div', 'quality') else None

        info = {'title':title, 'price':price, 'region':region, 'tag':tag}
        item_info.insert_one(info)
        url_list.update(
            {'url': url},
            {'url': url, 'is_crawler': True}
        )
        print(info)

#get_links_from('http://sz.58.com/shouji/', 1)
#get_item_info('http://zhuanzhuan.58.com/detail/775672374084042754z.shtml')