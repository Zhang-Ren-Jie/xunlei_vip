#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #

#author: downtownguy.hui@gmail.com
#date: 2015-07-20

from common import Singleton

class Configure(Singleton):
    '''
    ���ù����࣬���ڱ��������й������ö�Ӳ��������࣬�������ļ�����
    '''
    _VIP_URL = "http://www.521xunlei.com"
    _VIP_TITLE = u'������Ѹ�׺�'
    _VIP_PASS = u'�׷�����'
    
    def get_vip_url(self):
        return Configure._VIP_URL
    
    def get_vip_tile_target(self):
        return Configure._VIP_TITLE
    
    def get_vip_pass_target(self):
        return Configure._VIP_PASS
    
    def get_time_type(self):
        return 0
    