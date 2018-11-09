class Employee:
    '员工基类'

    emCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emCount += 1
        print("调用父类方法")

    def displayCount(self):
        print("Total Employee %d" % Employee.emCount)

    def displayEmployee(self):
        print("Name:", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("xjin", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
emp2.displayCount()
print("---------------------------------------")


class Manager(Employee):
    '父类'
    user = ()

    def __init__(self, name, salary):
        self.user = Employee(name, salary)

    def sayinfo(self):
        self.user.displayEmployee()

    def byeno(self, name):
        print("say Byebye to ", name)

    # def displayEmployee(self):
    #     print("over wirte parent's infomation\n")


boss = Manager("Gdir", 2000)
boss.sayinfo()
boss.displayEmployee()
print("---------------------------------------")
