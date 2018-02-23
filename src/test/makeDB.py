'''
Created on 2018年2月20日

@author: Administrator
'''
from test.person import Person, Manager
import shelve

db = shelve.open('persondB')
for key in db:
    print(db[key])
sue = db['sue jack']
sue.giveRise(0.2)
db['sue jack'] = sue


db.close()
