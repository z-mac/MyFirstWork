'''
Created on 2018年2月18日

@author: Administrator
'''
from .classTools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRise(self, percent):
        self.pay *= (1 + percent)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    
    def giveRise(self, percent, bonus = .10):
        Person.giveRise(self, percent + bonus)
        


