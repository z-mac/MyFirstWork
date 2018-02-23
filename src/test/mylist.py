'''
Created on 2018年2月23日

@author: Administrator
'''
from builtins import repr

class MyList(object):
    def __init__(self, start = []): 
        self.data = []
        for x in start: self.data.append(x)
    def __add__(self, other):
        return MyList(self.data + other)
    def __mul__(self, time):
        return MyList(self.data * time)
    def __getitem__(self, offset):
        return self.data[offset]
    def __len__(self):
        return len(self.data)
    def __getslice__(self, low, high):
        return MyList(self.data[low, high])
    def append(self, node):
        self.data.append(node)
    def __getattr__(self, name):
        return getattr(self.data, name)
    def __repr__(self):
        return repr(self.data)
    
        
        