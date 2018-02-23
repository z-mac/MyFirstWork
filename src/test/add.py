'''
Created on 2018年2月23日

@author: Administrator
'''

class Adder():
    def __init__(self, start = []): 
        self.data = start
    def add(self, y):
        print('Not Implemented')
    def __add__(self, other):
        return self.add(self.data, other)
        
class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        pass
        