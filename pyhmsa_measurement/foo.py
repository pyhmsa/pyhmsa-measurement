'''
Created on May 23, 2016

@author: Quantax
'''

class Descriptor:
    
    def __init__(self):
        self.abc = 123
    
    def __get__(self, instance, owner=None):
        print('__get__', self.abc, instance)
        return 'hello'
         
class Foo:
    
    var = Descriptor()
    
f = Foo()
print(f.var)