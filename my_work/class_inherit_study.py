class Telnet:
    def __init__(self, telnet_ip, id, pw):
        self.telnet_ip = telnet_ip
        self.id = id
        self.pw = pw

    def telnet_connect(self):
        telnet = Telnet(self.telnet_ip, 23)

    def execute_cmd(self, cmds):
        pass


class CiscoTelnet(Telnet):
    def __init__(self, telnet_ip, id, pw):
        super().__init__(telnet_ip, id, pw)

    def telnet_connect(self):
        print("cisco telnet connect 재정의")

    def execute_cmd(self, cmds):
        telnet = self.telnet_connect()
        print("cisco execute_cmd")


class DasanTelnet(Telnet):
    def __init__(self, telnet_ip, id, pw):
        super().__init__(telnet_ip, id, pw)

    def execute_cmd(self, cmds):
        print("dasan execute_cmd")



if __name__ == '__main__':
    # if equiup_type == "cisco":
    #     telnet = CiscoTelnet("1.1.1.1", "id", "pw")
    # elif equiup_type == "dasan":
    #     telnet = DasanTelnet("1.1.1.2", "id", "pw")

    telnet = DasanTelnet("1.1.1.2", "id", "pw")
    telnet.execute_cmd()





class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print("name : {}, age: {}".format(self.name, self.age), end='')

    def say(self):
        print("say")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def tell(self):
        super().tell()
        print(' Salary: "{}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def tell(self):
        super().tell()
        print(' 점수: {}'.format(self.marks))

if __name__ == '__main__':
    teacher = Teacher('jungil', '43', '400만원')
    teacher.tell()
    teacher.say()
    #
    # student = Student('jungil2', '13', 75)
    # student.tell()

    teacher1 = Teacher('teacher1', '31', '400만원')
    teacher2 = Teacher('teacher1', '32', '400만원')
    teacher3 = Teacher('teacher1', '33', '400만원')
    teacher4 = Teacher('teacher1', '34', '400만원')

    student1 = Student('student1', '13', 75)
    student2 = Student('student2', '14', 80)
    student3 = Student('student3', '15', 75)
    student4 = Student('student4', '16', 90)

    members = [teacher1, teacher2, teacher3, teacher4
               , student1, student2, student3, student4]

    for member in members:
        member.tell()