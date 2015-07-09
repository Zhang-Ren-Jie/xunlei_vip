#coding:gb2312
# ********************************** #
#          �������������                                                            #
#          ������ҵ��;                                                                #
#    ��ʹ�ñ�������ɵ��κ���ʧ�����˸Ų�����                      #
# ********************************** #

class Singleton(object):
    '''
    A Singleton base class
    thanks:http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
    StackOverFlow is an amazing website...^_^!
    '''
    _instance = None
    
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance