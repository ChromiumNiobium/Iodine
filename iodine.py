# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:43:22 2019

@author: zsc_c
"""

class player:
    def __init__(self,name):
        self.name=name
        self.life=3
        self.i=0
        self.he=False
        self.at=False
        self.cs=False
        self.live=3
        self.attacked=False
        self.attacks=set()
        self.die=False
        self.fang=set()
    def iodine(self):
        self.i+=1
    def helium(self):
        self.i-=1
        self.fudian()
        self.he=True
    def boron(self):
        pass
    def silicon(self):
        pass
    def vanadium(self):
        pass
    def molybdenum(self):
        pass
    def copper(self,a):
        a.attacks.add(0)
    def iron(self,a):
        self.i-=1
        self.fudian()
        a.attacks.add(1)
    def ruthenium(self,a):
        self.i-=2
        self.fudian()
        a.attacks.add(2)
    def osmium(self,a):
        self.i-=3
        self.fudian()
        a.attacks.add(3)
    def hassium(self,a):
        self.i-=4
        self.fudian()
        a.attacks.add(4)
    def polonium(self,a):
        self.i-=3
        self.fudian()
        if not 3 in a.fang:
            a.life-=3.00000000001
    def jiesuan(self):
        self.attacked=bool(self.live-self.life)
        if self.attacked==True and self.at==True or self.attacked==True and self.he==True:
            self.die=True
        if self.he:
            self.i+=2
        self.he=False
        self.attacked=False
        if self.life<=0:
            self.die=True
        self.live=self.life
        self.fang=set()
    def fudian(self):
        if self.i<0:
            self.life+=self.i
            self.i=0
            self.attacked=True
            if self.he or self.at or self.cs:
                self.gengxing('由于血量改变而死！')
        if self.life<=0:
            self.gengxing('负死了！')
    def die(self):
        self.die=True
    def gengxing(self,s):
        raise RuntimeError(self.name+s)
def main():
    n1=input('输入玩家1的名字：')
    n2=input('输入玩家2的名字：')
    exec(n1+'=player(\''+n1+'\')')
    exec(n2+'=player(\''+n2+'\')')
    while True:
        flag=0
        while not flag:
            s1=eval("input('输入'+'"+n1+"'+'在本回合的操作（小写）：')")
            try:
                eval(n1+'.'+s1)
                flag=1
            except TypeError:
                pass
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        flag=0
        while not flag:
            s2=eval("input('输入'+'"+n2+"'+'在本回合的操作（小写）：')")
            try:
                eval(n2+'.'+s2)
                flag=1
            except TypeError:
                pass
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        eval(n1+'.jiesuan()')
        eval(n2+'.jiesuan()')
        s=''
        if(eval(n1+'.die')==True):
            s+=n1+'输了！'
        if(eval(n2+'.die')==True):
            s+=n2+'输了！'
        if s!='':
            raise RuntimeError(s)
main()