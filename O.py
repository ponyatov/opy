# live object environment prototype.py

import os,sys
log = open(sys.argv[0]+'.log','w')

pool = [] # object pool

class Dat:
    def __init__(self,V,doc=''):
        global pool ; self.index = len(pool) ; pool.append(self) 
        self.val = V ; self.doc = doc
        self.attr = {} ; self.nest = []
    def head(self):
        return '<%s:%s> @%x # %s >%s' % (self.__class__.__name__.lower(),self.val, id(self), self.doc, self.index)
    def dump(self, depth=0):
        S = '\n' + '\t' * depth + self.head()
        for i in self.attr:
            S += '\n' + '\t' * (depth + 1) + '%s = ' % i
            S += self.attr[i].dump(depth+2)
        return S 
    def __repr__(self):
        return self.dump()
        
    def __setitem__(self, key, val):
        self.attr[key] = val

env = Dat('env',doc='global environment')

class Str(Dat):
    pass
    
env['MODULE']   = Str('opy')
env['ABOUT']    = Str('live object environment (prototype.py)')
env['AUTHOR']   = Str('Dmitry Ponyatov <dponyatov@gmail.com>')
env['GITHUB']   = Str('https://github.com/ponyatov/opy')

print >>log,pool
