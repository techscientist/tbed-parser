#!/usr/bin/env python2.5

from math import *

from dialogueAct import *
from transformation import *
        
class Rule:
    def __init__(self, trigger, transformation):
        self.trigger = trigger
        self.transformation = transformation
        
        return 
    
    def __str__(self):
        s = 'RULE:'
        s += str(self.trigger) #+'\n'
        s += str(self.transformation) 
        
        return s
        
    def __eq__(self, other):
        if not isinstance(other, Rule):
            return False
            
        if self.trigger == other.trigger and self.transformation == other.transformation:
            return True
        
        return False
        
    def __hash__(self):
        h = hash(self.trigger)
        h += hash(self.transformation)
        
        return h % (1 << 31) 
        
    def apply(self, da):
        # apply transformation on the dialogue act
        if self.trigger.validate(da):
            # applstr(each)+' Acc:'+str(each.acc)+' F:'+str(each.f)+'\n'y rules
            self.transformation.apply(da)
        
        return 
    
    def complexity(self):
        return self.trigger.complexity()+self.transformation.complexity()

    # cmp function for sort()
    def cmpPlx(self, r):
        ret = cmp(r.af,self.af)
        
        if ret == 0:
            ret = cmp(self.complexity(),r.complexity())
        
        return ret
    
    def setPerformance(self, af, acc, f):
        self.af = af
        self.acc = acc
        self.f = f
        
    @classmethod
    def read(cls, nRules):
        # constructor for lines
        
        nTriggers = filter(lambda r: r[1].startswith('Trigger:') != 0, nRules)
        nTrans = filter(lambda r: r[1].startswith('Transformation:') != 0, nRules)
        
        trigger = Trigger.read(nTriggers)
        trans = Transformation.read(nTrans)
        
        return cls(trigger, trans)
        
    def write(self, i):
        s = 'Rule:%d\n' % i
        s+= self.trigger.write()
        s+= self.transformation.write()
        
        return s

def getRules(da, tplGrams):
    # explode trans & triggers
    rules = []
    for tran in da.genTrans():
        for trigger in da.genTriggers(tplGrams):
            r = Rule(trigger, tran)
            rules.append(r)
    
    return rules
