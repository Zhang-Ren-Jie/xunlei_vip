#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #

#author: downtownguy.hui@gmail.com
#date: 2015-07-20
import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))

def main():
    launcher_path = os.path.join(current_path, "../source")
    sys.path.insert(0, launcher_path)
    from xlVIP import  run as launcher_main
    launcher_main()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()