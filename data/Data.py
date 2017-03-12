import uuid
import random
import json
import sys
import getopt

def computePrego(actor):
    if(actor.sex == 'F' and actor.age > 14):
        return True
    else:
        return False

class Entity(object):
    def __init__(self):
        self.id = uuid.uuid4()

class Actor(Entity):
    def __init__(self, name, hitpoints, age, sex = 'U', mother = None, father = None):
        Entity.__init__(self)
        self.age = age
        self.name = name
        self.hitpoints = hitpoints
        self.mother = mother
        self.father = father
        s = sex
        if(sex == 'U'):
            s = 'M' if(random.randint(0,1) == 0) else "F"
        self.sex = s
        self.preg = computePrego(self)
    def isAlive(self):
        return self.hitpoints > 100
    def hit(self, damage):
        self.hitpoints = self.hitpoints - damage



class Person(Actor):
    def __init__(self, name, sex = 'U', age = random.randint(0,120), mother = None, father = None ):
        Actor.__init__(self, name, 100, sex = sex, age = age, mother = mother, father = father)
        self.name = name

class Orc(Actor):
    def __init__(self, name, age = random.randint(0,120) ):
        Actor.__init__(self, name, hitpoints=200, age = age)
        self.name = name


def prego(people):
    females = filter(lambda x: x.sex == 'F', people)
    for x in females:
        x.age = 44


def main():
    # parse command line options
    bob = Person("Bob", 'M')
    kathy =  Person("Kathy", 'F')
    slash = Orc("Slash")

    print("name: ",bob.name, bob.id, bob.sex)
    print("name: ",slash.name, slash.id, slash.sex)

    billy = Person("Billy",age = 0, father = bob, mother = kathy)


    town = [Person("person:") for x in range(10)]
    #print(json.dumps(town, default=lambda o: o.__dict__))

    females = filter(lambda x: x.sex == 'F',town)
    prego(town)
    print(json.dumps(town, default=lambda o: o.__dict__, indent=4))


    #print("slash: ",slash.isAlive())
    #slash.hit(400)
    #print("slash: ",slash.isAlive())
    #print(json.dumps(billy, default=lambda o: o.__dict__))

if __name__ == "__main__":
    main()






