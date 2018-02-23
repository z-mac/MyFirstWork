'''
Created on 2018年2月20日

@author: Administrator
'''

class AttrDisplay:
    def __init__(self):
        pass
    
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, self.__dict__[key]))
        return ','.join(attrs)
    
    def __str__(self):
        return '%s:%s' % (self.__class__.__name__, self.gatherAttrs())
    

if __name__ == '__main__':
    class TopClass(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopClass.count
            self.attr2 = TopClass.count + 1
            TopClass.count += 2
    
    class SubClass(TopClass):
        pass
    
    X, Y = TopClass(), SubClass()
    print(X)
    print(Y)