#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #

#author: downtownguy.hui@gmail.com
#date: 2015-07-20

from crawl import Crawl

def run():
    crawler = Crawl()
    vips = crawler.all_come_to_bowl()
    print_vips(vips)

def print_vips(vips):
    print vips
        
if __name__=="__main__":
    run()