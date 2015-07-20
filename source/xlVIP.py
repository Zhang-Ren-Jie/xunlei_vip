#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #

#author: downtownguy.hui@gmail.com
#date: 2015-07-20

###########################################
# ��������ͼ�λ��ģ��о������û�б�Ҫ�������ն�ģʽ��ֱ�Ӹ��ư�#
# �Ժ��о����ڸĽ�������ֱ�ӵ����½ʱ��������                                        #
###########################################
from crawl import Crawl
import ctypes
import sys

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

FOREGROUND_DARKWHITE = 0x07 # dark white.
FOREGROUND_GREEN = 0x0a # green.
FOREGROUND_RED = 0x0c # red.
FOREGROUND_BLUE = 0x09 # blue.

def run():
    crawler = Crawl()
    vips = crawler.all_come_to_bowl()
    print_vips(vips)

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
 
def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool
 
#reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)


#dark white
def printDarkWhite(mess):
    set_cmd_text_color(FOREGROUND_DARKWHITE)
    sys.stdout.write(mess)
    resetColor()

#green
def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess)
    resetColor()
    
def printColor(mess, type):
    if type == 0:
        printDarkWhite(mess)
    else:
        printGreen(mess)
        
def print_vips(vips):
    cid = 0
    for vip in vips:
        printColor("%s\t\t%s\n" % (vip[0], vip[1]), cid)
        cid = ~cid
        
if __name__=="__main__":
    run()