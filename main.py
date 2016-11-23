from multiprocessing import Pool
from channel_extract import channel_list
from pages_parsing import get_links_from,get_item_info
from pages_parsing import url_list


def get_all_links_from(channel):
    for i in range(1, 101):
        get_links_from(channel, i)

if __name__ == '__main__':
    pool = Pool()
    pool.map(get_item_info, [item['url'] for item in url_list.find({'is_crawler': None})])


