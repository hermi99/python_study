
class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hello {}".format(self.name))


if __name__ == '__main__':
    # person1 = Person()
    # person2 = Person()
    # print("person1:", person1)
    # print("person2:", person2)

    person1 = Person("jungil")
    person1.say_hi()
