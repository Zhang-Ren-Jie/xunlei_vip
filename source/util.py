#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #

from config import Configure

class Util(object):
    '''
    �����࣬��ô���ƶ�����������������ӣ�doubi
    '''
    config = Configure()
    @staticmethod  
    def get_time():
        if Util.config.get_time_type() == 0:
            return Util._get_system_time()
        else:
            return Util._get_network_time()
    @staticmethod  
    def _get_system_time():
        return (7, 9)
    
    @classmethod
    def _get_network_time():
        return (7, 9)