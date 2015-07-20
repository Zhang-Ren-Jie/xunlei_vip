#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #

#author: downtownguy.hui@gmail.com
#date: 2015-07-20

from config import Configure
from util import Util

import urllib2
import re
 
class Crawl(object):
    '''
    ץȡ�ṩVIP��վ����ҳ����ȡ������û����������б�
    ��ȷ���Լ�������ʱ��ͬ��ǰ������ʱ��������Ժ���ܻ����Ϊ�����ȡʱ�䣩
    '''
    def __init__(self):
        self.config = Configure()
        self.errors = []
        self.meta = {'info':'', 'real_url':'', 'code':0}
        
    def _get_content(self, url):
        '''
        ��ȡ��ҳ����
        '''
        i_headers = {"User-Agent" : "Mozilla/5.0 (windows; U; Windows NT 5.1; zh-CN; rv:1.9.1)\
                  Gecko/20090624 Firefox/3.5", "Accept" : "text/plain"}
        req = urllib2.Request(url, headers = i_headers)
        try:
            response = urllib2.urlopen(req, timeout = 30)
        except urllib2.HTTPError, e:
            self.err.append(e)
        except urllib2.URLError, e:
            self.err.append(e)
        else:
            self.meta['info'] = response.info()
            self.meta['real_url'] = response.geturl()
            self.meta['code'] = response.getcode()
            if self.meta['code'] == 200:
                cont = response.read()
                return cont.decode("GBK")
            else:
                print self.meta['code']
                return None
        return None
    def _get_day_link(self):
        '''
        ��ȡ����ķ�������
        '''
        cur_day = Util.get_time()
        if cur_day == None:
            self.errors.append('Get sys-time error')
            return []
        mainpage = self._get_content(self.config.get_vip_url())
        if mainpage != None:
            #first try to find year-month-day published
            time_str = '-'.join(cur_day)
            #print time_str
            re_str = '<em>%s</em>.*</a></label> <a href="(.*\.html)"' % time_str
            #print re_str
            links = self._get_links(mainpage, re_str)
            if len(links) != 0:
                #ok, no need more
                pass
            else:
                #seconf try to find year-mond-(day-1) published for the next day
                day_before = Util.get_day_before(cur_day)
                chars = self._gen_choices(cur_day)
                time_str = '-'.join(day_before)
                re_str = '<em>%s</em>.*</a></label> <a href="(.*\.html)" title=".*[%s].*"' % (time_str, '|'.join(chars))
                links = self._get_links(mainpage, re_str)
            return links
        return []
    
    def _get_links(self, page, re_str):
        time_re = re.compile(re_str)
        links = re.findall(time_re, page)
        return links
    
    def _gen_choices(self, cur_day):
        '''
        ��ȡǰһ�췢���Ľ�����������
        '''
        return ['%s��' % cur_day[2], '%s��' % cur_day[2]]
     
    def _get_vips(self, url):
        '''
        ��ȡĳһҳ������VIP�˺�����
        '''
        page = self._get_content(url)
        re_str = '(\w+:\d)\D+(\d+)<br />'
        #print re_str.decode('utf-8')
        vips = self._get_links(page, re_str)
        return vips
        
    def all_come_to_bowl(self):
        '''
        vips come to my bowl quickly
        '''
        links = self._get_day_link()
        ret = []
        for link in links:
            cur_vips = self._get_vips(self.config.get_vip_url() + "/" + link)
            ret.extend(cur_vips)
        return ret
        