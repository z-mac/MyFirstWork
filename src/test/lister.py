'''
Created on 2018年2月22日

@author: Administrator
'''

#!/usr/bin/python
# -*- coding: utf-8 -*-

class ListInstance(object):
    '''
    Mix-in class that provides a formatted print() or str() of 
    instances via inheritance of __str__, coded here; displays 
    instance attrs only; self is the instance of lowest class; 
    uses __X names to avoid clashing with client's attris
    '''
    
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (self.__class__.__name__, id(self), self.__attrnames())
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname= %s=%s\n' % (attr, self.__dict__[attr])
        return result

        