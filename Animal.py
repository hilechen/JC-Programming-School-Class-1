'''
Superhero > Nome > Falcon > Mammoth > Cat > Superhero

Superhero + Nome = Falcon
Nome + Falcon = Mammoth
Falcon + Mammoth = Cat
Mammoth + Cat = Superhero
Cat + Superhero = Nome

Falcon - Nome = Superhero
Falcon - Superhero = Nome
Mammoth - Falcon = Nome
Mammoth - Nome = Falcon
Cat - Falcon = Mammoth
Cat - Mammoth = Falcon
Superhero - Cat = Mammoth
Superhero - Mammoth = Cat
Nome - Cat = Superhero
Nome - Superhero = Cat

Check class for object example:
if 'Cat' in str(type(self)) # check if self is a Cat object


'''


import random

class Animal:
    def __init__(self,name,sound = "", status = 'alive', age = 0):
        self.name=name
        self.sound = sound
        self.status = status
        self.age = age
        print('\n'+name,'was born','\n')
    def die(self):
        self.status = 'dead'
        print(self.name,'died')
    def make_sound(self):
        if self.status != "dead":
            print(self.name, 'said',self.sound)
    def grow(self, years=1):
        self.age += years
    def __str__(self):
        res = ''
        for i in self.__dict__.keys():
            res += i+ ' : ' + str(self.__dict__[i])+'\n'
        return res
        
    def kill(self,other_animal):
        print(self.name,'killed',other_animal.name)
        other_animal.die()

    def __gt__(self, other):
        c1 = str(type(self)).replace('<class \'__main__.', '').replace('\'>', '')
        c2 = str(type(other)).replace('<class \'__main__.', '').replace('\'>', '')
        return (c1,c2) == ('Superhero', 'Nome') or \
            (c1,c2) == ('Nome', 'Falcon') or \
            (c1,c2) == ('Falcon', 'Mammoth') or \
            (c1,c2) == ('Mammoth', 'Cat') or \
            (c1,c2) == ('Cat', 'Superhero')                  

class Cat(Animal):
    def __init__(self, name, sound = 'meow', status = 'alive', age = 0, life_count = 9):
        
        super().__init__(name, sound)
        self.life_count = life_count
        
    def die(self):
        if self.life_count > 1:
            self.life_count -= 1
            self.age = 0
        else:
            super().die()

class Mammoth(Animal):
    def __init__(self, name, sound = 'murrr', status = 'alive',load = 50, load_unit = 'kg', Age = 5):
        super().__init__(name, sound, age = Age)
        self.load = load
        self.load_unit = load_unit
    def grow(self,years):
        super().grow(years)
        self.load += 2* years
    def __str__(self):
        res = ''
        for i in self.__dict__.keys():
            if i == 'load':
                res += ' load: ' + str(self.__dict__[i])+self.load_unit + '\n'
            res += i+ ' : ' + str(self.__dict__[i])+'\n'
        return res
class Falcon(Animal):
    def __init__(self, name, wingspan, length, species, strength, health, sound = "kaw", status = "alive", killcount = 0, age = 0):
        super().__init__(name, sound, status, age)
        self.wingspan = wingspan
        self.length = length
        self.strength = strength
        self.health = health
        self.killcount = killcount
    def grow(self, num):
        self.age += num
        if self.age < 7:
            self.wingspan += 2 * num
            self.length += 2 * num
            self.strength += 1.5 * num
            self.health -= 2 * num
        elif self.age > 7 and self.age <= 25:
            self.wingspan -= 0.5 * num
            self.length -= 0.5 * num
            self.strength - 0.5 * strength
            self.health -= 7
        elif self.age > 25:
            self.wingspan -= num
            self.length -= num
            self.strength  -= 1.5 * num
            self.health -= 10 * num
        if self.strength <= 0 and self.health <= 0:
            self.status = "dead"
            self.strength = 0
            self.health = 0
    def dive(self, num, accuracy):
        for i in range(num):
            if random.randint(1,100) <= 100*accuracy:
                self.killcount += 1

class Superhero(Animal):
    def __init__(self, identity,mental_health, powers, fame, celeb=False,invincible=True):
        super().__init__(identity)
        self.invincible=invincible
        self.mental_health=mental_health
        self.powers=powers
        self.fame=fame
        self.celeb=celeb
    def die(self):
        pass


class Nome(Animal):
    def __init__(self,name,sound = "", status = 'alive', age = 10000000,iq = 5,special = 'played dead'):
        super().__init__(name,sound,status,age)
        self.iq = iq
        self.special = special
    def Special(self):
        print(self.name, self.special)
    def learn_magic(self):
        if 'g' in self.name.lower():
            print(self.name, 'blew himself up while learning magic')
            self.iq -= 1
        else:
            print(self.name,'learned magic and gained 5 IQ')
            self.iq += 5
    def kill(self,other_animal):
        if 'g' in self.name.lower():
            print(self.name,'tried to kill',other_animal.name,'but failed')
        else:
            super().kill(other_animal)
    def __str__(self):
        res = ''
        for i in self.__dict__.keys():
            if i == 'special':
                continue
            res += i+ ' : ' + str(self.__dict__[i])+'\n'
        return res
    def grow(self,years=1):
        print(self.name,'tried to grow but he has no age')
    def die(self):
        print(self.name,'cannot die because he is invincible')

print('Cat is created')
c = Cat('tac', age = 2)
print(c)
c.die()
print(c)
print('======================')
print('Mammoth is created')
m = Mammoth('Chip')
print(m)
m.grow(1)
print(m)
print('======================')
print('Falcon is created')
f = Falcon("Joe", 8, 7, "Peregrine Falcon", 7, 100)
print(f)
f.grow(6)
print(f)
f.dive(1000, .8)
print(f)
print('======================')
print('Nome is created')
n = Nome('Nome',sound = 'grunt',special = 'did the orange justice')
print(n)
n.Special()
n.learn_magic()
n.kill(c)
print(n)
print(c)
n2 = Nome('Gnome',sound = 'Meow',special = 'tripped and fell')
print(n2)
n2.Special()
n2.learn_magic()
n2.kill(c)
n2.grow()
n2.make_sound()
print(n2)
print(c)
f.kill(n)
f.kill(n2)
print('======================')
print('Superhero is created')
bill=Superhero('bill',200,'flying','lasagna','4000000 fans', True,)
print('bill crashed to earth')
print(bill)
y=1000000000000000000000000
bill.grow(y)
print(bill)
print('bill is still saving earth after '+str(y)+' years')

print(c > bill)





