"""
class Sd:
 ''' this doc string..'''
print(Sd.__doc__)
help(Sd)
"""
'''
class Student:
        def __init__(self,sno,sname,smarks):
                self.sno=sno
                self.sname=sname
                self.smarks=smarks
        def info(self):
         #for every method self is the compulsary argument
                print("Student No :",self.sno)   
                print("Student Name :",self.sname)   
                print("Student Marks :",self.smarks)    
s1=Student(100,'shivani',99)
s2=Student(200,'shalini',95)  
s1.info() #here we are not pasing any argument
s2.info()
'''
'''
class Test:
        def __init__(self):
                print("Default constructor exicuted.")
        def __init__(self,name):
                self.name=name
                print("Constructor with one Arg",self.name)
t=Test()
t1=Test("shivam")
'''
'''
#methods and variables in python 

class Student:                                          
        clgname="SGGS" #class variable
        def __init__(self,sno,sname,smarks): #local variables >> sno,sname,smarks
                self.sno=sno   #instance variable
                self.sname=sname  #instance variable
                self.smarks=smarks  #instance variable
        def display(self):
         #for every method self is the compulsary argument
                self.dept="cse"  #instance variable
                print("Student No :",self.sno)   
                print("Student Name :",self.sname)   
                print("Student Marks :",self.smarks)  
        @classmethod #decorator indicating class method.
        def getClgName(cls): #class level object -> cls 
                print("college name :",cls.clgname)
                  
        @staticmethod  #static method decorator
        def averege():
                x=10 #local variables
                y=20
                ave=(x+y)/2
                print("average : ",ave)
        def averege1(): #another static mthod without decorator
                x=10 #local variables
                y=20
                ave=(x+y)/2
                print("average : ",ave)
s1=Student(100,'shivani',99)
s1.display()
Student.getClgName()  #called using class name.
s2=Student(200,'shalini',95)  
s2.display()
Student.getClgName()  #calling the class level method.    
s1.averege() #calling static methos
#Student.averege1() #calling static method withot @staticmethod
print(s1.__dict__) #print all the instance variable created for an object.
'''
''' 
class Student:
        def __init__(self,name):
                self.name=name
                self.lapObject=self.Laptop   #creating laptop object inside the student constructor. here for evey object of student one laptop class object gets created.
        def show(self):
                print(self.name)
                self.lapObject.display()
        class Laptop:
                def __init__(self):
                        self.brand="Dell"
                        self.ram=8
                def display(self):
                        print(self.brand,self.ram)
s1=Student('shiv')
s2=Student('tulip')
s1.show()'''

#inheritance.
#1.Single Level Inheritance....
'''
class A:
        def feature1(self):
                print("feature 1 here")
        def feature2(self):
                print("feature 2 here")
class B(A):
        def feature3(self):
                print("feature 3 here")
        def feature4(self):
                print("feature 4 here") 
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4() 
'''

#2.Multi Level Inheritance....
'''
class A:
        def feature1(self):
                print("feature 1 here")
        def feature2(self):
                print("feature 2 here")
class B(A):
        def feature3(self):
                print("feature 3 here")
        def feature4(self):
                print("feature 4 here")
class C(B):
        def feature5(self):
                print("feature 5 here")
        def feature6(self):
                print("feature 6 here")
c1=C() 
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6() 
'''
#3.Multiple Level Inheritance....
'''
class A:
        def feature1(self):
                print("feature 1 here")
        def feature2(self):
                print("feature 2 here")
class B():
        def feature3(self):
                print("feature 3 here")
        def feature4(self):
                print("feature 4 here")
class C(A,B):
        def feature5(self):
                print("feature 5 here")
        def feature6(self):
                print("feature 6 here")
c1=C() 
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()
'''
#variable length argument passing.....
'''
#def functionName(*args):
class student:
        def __init__(self,name,*age): #age is the tuple which means it allows us to provide any no. of arguments
                self.name=name
                print(self.name)
                print(age,type(age))
s0=student('tulip')
s1=student('shivani','tulip','tittu')
'''
'''
#setting default arguments...
class student:
        def __init__(self,name='shivani'): #default argument 'name' is passed 
                self.name=name
                print(self.name)

s0=student('tulip') #prints tulip
s1=student() #prints shivani
'''
'''
#def functionName(**kwargs):
class student:
        def __init__(self,name,**data): #age is the tuple which means it allows us to provide any no. of arguments
                self.name=name
                print(self.name)
                print(data,type(data))
                for i,j in data.items():
                        print(i,j)
s0=student('tulip') #only name and an empty dictionary is passed 
s1=student('shivani',tulip='daisy',shiv='shankar') #shivani name and a dictionary is passed.
  '''
'''
num1=5
num2=4
while(num2>=1):
        print("*")
        for index in range(1,num1+1):
                print("*")
                num2-=1
        print("*")          
'''
'''
class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input("Enter No of students : "))
for i in range(n):
    print("Enter name of student :")
    name=input()
    print("name :" ,name)
    marks=int(input("Enter marks of students : "))
    s=Students()
    s.setName(name)
    s.setMarks(marks) 
'''
'''
#Inner Classes
class Outer(object):
    """inner class concept"""
    def __init__(self):
        print("Outre class...")
    def m2(self):
        print("Instance method in outer class")
    
    class Inner:   #inner class
        def __init__(self):
            print("Inner class constructor..")
        def m1(self):
            print("Inner class Method..")

"""o=Outer()  # one way
i=o.Inner()

i=Outer().Inner() #another way
i.m1()"""

Outer().Inner().m1()  #Third way 
'''
'''
#Second Example of Inner class
class person:
    def __init__(self):
        self.name="shvani"
        self.dob=self.DOB()
    def display(self):
        print("Name:{}".format(self.name))
        self.dob.display()

    class DOB:
        """Inner class DOB"""
        def __init__(self):
            self.dd=29
            self.mm=02
            self.yy=2000

        def display(self):
            print("DOB={}/{}/{}".format(self.dd,self.mm,self.yy))
p=person()
p.display()

'''
class demo:
  def __init__(self):
    self.a=10 #public variable
    self._b=20 #this in only a convention it acts as public variable we can access it ouside the class
    self.__c=30 #private variable here we cant access data outside the class
c=demo()
print(c.a)
print(c._b)
print(c.__c)
