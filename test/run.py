#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #
from crawl import Crawl

def run():
    crawler = Crawl()
    vips = crawler.all_come_to_bowl()
    print_vips(vips)

def print_vips(vips):
    for vip in vips:
        print "�û�����%s\t���룺%s" % (vip[0], vip[1])
        
if __name__=="__main__":
    run()