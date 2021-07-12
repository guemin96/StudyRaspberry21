class person(object):
    total = 0

    def __init__(self, name, age): 
        self.name = name;
        self.age = age;

    def getAge(self):
        return self.age