'''
Created on 2018年2月18日

@author: Administrator
'''
# -*- coding: utf-8 -*-

from test.add import Adder, ListAdder, DictAdder
from test.mylist import MyList


if __name__ == '__main__':
    x = MyList('spam')
    print(x)
    print(x + [2])
    print(x * 2)
    print(x[2])
    print(x[:-1])
    print(x + ['eggs'])
    print(x.append('xxxxx'))
    x.sort()
    print(x)
    
    
    
    
