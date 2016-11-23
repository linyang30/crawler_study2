from bs4 import BeautifulSoup
import requests


second_hand_main_page_url = 'http://sz.58.com/sale.shtml'
host_url = 'http://sz.58.com'

def get_channel_url(url):
    web_reponse = requests.get(url)
    soup = BeautifulSoup(web_reponse.text, 'lxml')
    links = soup.select('ul.ym-submnu > li > b > a')
    for link in links:
        page_url = host_url + link.get('href')
        print(page_url)
#get_channel_url(second_hand_main_page_url)

channel_list ='''
    http://sz.58.com/shouji/
    http://sz.58.com/tongxunyw/
    http://sz.58.com/danche/
    http://sz.58.com/fzixingche/
    http://sz.58.com/diandongche/
    http://sz.58.com/sanlunche/
    http://sz.58.com/peijianzhuangbei/
    http://sz.58.com/diannao/
    http://sz.58.com/bijiben/
    http://sz.58.com/pbdn/
    http://sz.58.com/diannaopeijian/
    http://sz.58.com/zhoubianshebei/
    http://sz.58.com/shuma/
    http://sz.58.com/shumaxiangji/
    http://sz.58.com/mpsanmpsi/
    http://sz.58.com/youxiji/
    http://sz.58.com/jiadian/
    http://sz.58.com/dianshiji/
    http://sz.58.com/ershoukongtiao/
    http://sz.58.com/xiyiji/
    http://sz.58.com/bingxiang/
    http://sz.58.com/binggui/
    http://sz.58.com/chuang/
    http://sz.58.com/ershoujiaju/
    http://sz.58.com/bangongshebei/
    http://sz.58.com/diannaohaocai/
    http://sz.58.com/bangongjiaju/
    http://sz.58.com/ershoushebei/
    http://sz.58.com/yingyou/
    http://sz.58.com/yingeryongpin/
    http://sz.58.com/muyingweiyang/
    http://sz.58.com/muyingtongchuang/
    http://sz.58.com/yunfuyongpin/
    http://sz.58.com/fushi/
    http://sz.58.com/nanzhuang/
    http://sz.58.com/fsxiemao/
    http://sz.58.com/xiangbao/
    http://sz.58.com/meirong/
    http://sz.58.com/yishu/
    http://sz.58.com/shufahuihua/
    http://sz.58.com/zhubaoshipin/
    http://sz.58.com/yuqi/
    http://sz.58.com/tushu/
    http://sz.58.com/tushubook/
    http://sz.58.com/wenti/
    http://sz.58.com/yundongfushi/
    http://sz.58.com/jianshenqixie/
    http://sz.58.com/huju/
    http://sz.58.com/qiulei/
    http://sz.58.com/yueqi/
    http://sz.58.com/chengren/
    http://sz.58.com/nvyongpin/
    http://sz.58.com/qinglvqingqu/
    http://sz.58.com/qingquneiyi/
    http://sz.58.com/chengren/
    http://sz.58.com/xiaoyuan/
    http://sz.58.com/ershouqiugou/
    http://sz.58.com/tiaozao/
    '''