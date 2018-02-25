'''
Created on 2018年2月18日

@author: Administrator
'''
# -*- coding: utf-8 -*-
class FormatError(Exception):
    logfile = 'formaterror.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    
    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at', self.file, self.line, file = log)
    
def parser():
    raise FormatError(42, 'spam.txt2')


def main():
    try:
        parser()
    except FormatError as exc:
        exc.logerror()
    print('ok')

if __name__ == '__main__':
    main()
    
    
    
    
