#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #
from common import Singleton

class Configure(Singleton):
    '''
    ���ù����࣬���ڱ��������й������ö�Ӳ��������࣬�������ļ�����
    '''
    _VIP_URL = "www.521xunlei.com"
    
    def get_vip_url(self):
        return Configure._VIP_URL
    
    def get_time_type(self):
        return 0
    