class Student:
    # name = "John Doe"
    def __init__(self,name,school):
        print('I am in parent')
        self.name = name
        self.school = school
        self.marks = []
    def add_mark(self):
        return sum
    
st = Student("John","XYZ School")        

class WokringStudent(Student):
    def __init__(self,name,school,salary):
        print("In Working Student")
        super().__init__(name,school)
        self.salary = salary
    def display(self):
        self.marks = self.marks + [40,50,60]
        print(sum(self.marks)//len(self.marks))
        return f"Name: {self.name}, School: {self.school}, Salary: {self.job}"  
    @property  #convert method to property
    def weekly_salary(self):
        return self.salary * 40
    
ls = WokringStudent("Jane","ABC School",5000)  
print(ls.weekly_salary)
#print(WokringStudent.weekly_salary(ls))

class Foo:
    def __init__(self,name):
        self.name = name
    @classmethod
    def bar(cls,x):
        print(cls.__name__)
        print(x)
        
        # print(':::::',self.name)  # will give error as class method do not have selfs
ls = Foo('')
Foo.bar('100')        

##Static Method
class Bar:
    @staticmethod
    def baz():
        print("I am in static method")
br = Bar()        
Bar.baz()       
br.baz()