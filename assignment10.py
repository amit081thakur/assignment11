# Q.1- Create a class Animal as a base class and define method animal_
# attribute. Create another class Tiger which
# is inheriting Animal and access the base class method.

class animal:
    leg = 0
    eye = 0
    name = "animal"
    def animal_attribute(self):
        print(self.name + " has %d legs" %self.leg)
        print(self.name + " has %d eyes"  %self.eye)
class tiger(animal):
    leg = 4
    eye = 2
    name = "tiger"
a = tiger()
a.animal_attribute()


#Q.2- What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())

# answer is          A B
#                     A B


#Q.3- Create a class Cop. Initialize its name, age , work experience and designation.
#  Define methods to add, display and update the following details. Create another
#  class Mission which extends the class Cop. Define method add_mission _details.
# Select an object of Cop and access methods of base class to get information for a
# particular cop and make it available for mission.

class cop:

    coplist = ({1,2,3})
    def __init__(self,age = None,name = None,work_experience = None,designation = None):
        if age == None:
            None
            print("no record")
        else:
            self.name = str(input("update name = "))
            self.age = int(input("update age= "))
            self.work_experience = int(input("update experience = "))
            self.designation = str(input("update designation= "))
            self.coplist1 = list([age, name, work_experience, designation])
            print("record entered")

    def display(self):
        print("name : {}".format(self.name))
        print("age : {}".format(self.age))
        print("work_experience: {}".format(self.work_experience))
        print("designation : {}".format(self.designation))

    def update(self):
        while a == True:
            print("0. Exit[Y/N]" " 1.name  2.age 3.work_experience 4.designation( enter in range(0,5))")
            copchoice = int(input("__"))
            Next = input("__")
            if copchoice == 0:
                a = True
            else:
                for x,val in cop.coplist,self.coplist1:
                    if x == copchoice:
                        self.coplist1[x] = Next
                        print("successfully updated")
        self.display()
    def adddetail(self):
        name = str(input("enter  name = "))
        age = int(input( "enter age= "))
        work_experience = int(input("enter  experience = "))
        designation = str(input("enter  designation= "))
        self.name = name
        self.age = age
        self.work_experience = experience
        self.designation = designation
        self.coplist1 = list([name,age,work_experience,designation])
        print("new record entered")
        self.display()
class mission(cop):
    def __init(self):
        super
    def __adddetail(self):
        if self.age <48:
            self.mission_detail = input("about mission:")
            print("mission added")
        else:
            print("overflow")
    def display_mission(self):
        print("mission: {}". format(self.missiondetail))

q = mission()
q.display()
q.update()

w = mission()
w.adddetail()

#q4 =

class shape():
    def __init(self,len,bre):
        area(self.len,self.bre)


    def area(self,len,bre):
        self.len = len
        self.bre = bre

class rectangle(shape):
    def __init(self):
        super
    def area(self,len,bre):
        return(self.len*self.bre)
class square(shape):
    def __init__(self):
        super
    def area(selfself,side):
        return(4*self.side)

shape1 = rectangle()
print("area of rectangle : {}".format(shape1.area(4,4)))
shape1 = square()
print("area of square  :  {} ".format(shape1.area(4,4)))







