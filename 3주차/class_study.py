

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("name = {}, age = {}".format(self.name, self.age))

    def test(self):
        self.print()


if __name__ == '__main__':
    # person = Person()
    # print(person)
    # # print(person.name, person.age)
    # person.print()
    #
    # person.age = 30
    #
    # person.print()
    #
    #
    # person1 = Person()
    # print(person1)
    # person1.age = 50
    # person1.print()

    person = Person("jungil", "age")
    person.print()

    person1 = Person("jungil2", "40")
    person1.print()





