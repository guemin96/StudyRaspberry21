import time
import Person

number = [10, 20, 30]
print(dir(number))

p = Person.Person('Park',26)
print(p.age)
print(p.name)
print(p.getAge())
print(p.total)

john = Person.Person("John Doe", 35)
print(john.name)
