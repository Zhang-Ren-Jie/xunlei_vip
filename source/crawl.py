#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #
from config import Configure
from util import Util



class Crawl(object):
    '''
    ץȡ�ṩVIP��վ����ҳ����ȡ������û����������б�
    ��ȷ���Լ�������ʱ��ͬ��ǰ������ʱ��������Ժ���ܻ����Ϊ�����ȡʱ�䣩
    '''
    def __init__(self):
        self.config = Configure()
    
    def _get_content(self, url):
        '''
        ��ȡ��ҳ����
        '''
        return None
    def _get_day_link(self):
        '''
        ��ȡ����ķ�������
        '''
        cur_day = Util.get_time()
        return ["thread-6785-1-1.html", "thread-6787-1-1.html"]
    
    def _get_vips(self, url):
        '''
        ��ȡĳһҳ������VIP�˺�����
        '''
        return [('hehe', 'f..k'), ('haha', 'm..m')]
        
    def all_come_to_bowl(self):
        '''
        vips come to my bowl quickly
        '''
        links = self._get_day_link()
        ret = []
        for link in links:
            cur_links = self._get_vips(self.config.get_vip_url() + "/" + link)
            ret.append(cur_links)
        return ret
        