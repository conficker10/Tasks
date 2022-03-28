class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.place = None

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age} and Place: {self.place}'

class PersonBuilder:
    def __init__(self, person = Person()):
        self.person = person

    def set_name(self, name):
        self.person.name = name
        return self
    
    def set_age(self, age):
        self.person.age = age
        return self

    def set_place(self, place):
        self.person.place = place
        return self

    def build(self):
        return self.person


if __name__ == '__main__':
    pb = PersonBuilder()
    person = pb.build()
    print(person) 
    person = pb.set_name('Mr ABC').set_age(22).build()
    print(person)

    pb2 = PersonBuilder(person)
    print(pb2.set_place('XYZ').build())