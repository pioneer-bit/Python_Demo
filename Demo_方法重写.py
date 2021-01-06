# Author:丁泽盛
# data:2020/10/2 13:47
class Person(object):#Person继承Object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super().info()
        print(self.stu_no)


class Teacher(Person):
    def __init__(self,name,age,teacheroyear):
        super().__init__(name,age)
        self.teacheroyear = teacheroyear
    def info(self):
        super().info()
        print('教龄',self.teacheroyear)

stu=Student('张三',20,'1001')
teacher=Teacher('李四',34,12)

stu.info()
print('+++++++++++++______________________+++++++++++++++')
teacher.info()


print(stu)