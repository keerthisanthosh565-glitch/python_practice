# # # # student_1 = "keerthi"
# # # # student_1_age = 24
# # # # student_2 = "grace"
# # # # student_2_age = 21
# # # # student_3 = "krishna"
# # # # student_3_age = 24
# # # # student_4 = "anjali"
# # # # student_4_age = 21
# # # # student_5 = "darshna"
# # # # student_5_age = 23

# # # # print(student_1, student_1_age)
# # # # print(student_2,student_2_age)
# # # # print(student_3,student_3_age)
# # # # print(student_4,student_4_age)
# # # # print(student_5,student_5_age)

# # # class student:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age

# # # student_1= student("krishna",24)
# # # print(student_1.name,student_1.age)

# # # def ___init__(self,name,age):
# # #     self.name = name
# # #     self.age = age

# # # # student_1 = student("Aakash",21)
# # # # print(student_1.name)
# # # # student_2 = student("Vishnu",22)
# # # # print(student_2.name)
# # # # student_3 = student("Arjun",23)
# # # # print(student_3.name)
# # # # student_4 = student("Abinav",24)
# # # # print(student_4.name)
# # # # student_5 = student("Dhanesh",25)
# # # # print(student_5.name)


# # # class book:
# # #     def  __init__(self,name,author,pages,year):
# # #         self.name= name
# # #         self.author = author
# # #         self.pages = pages
# # #         self.year = year

# # #     # book_1 = book("aadujeevitham","grace",400,2010)
# # #     # print(book_1.name,book_1.author,book_1.pages,book_1.year)


# # # # class Employee:
# # # #     def __init__(self, name, salary, id_no, job_role, joining_date):
# # # #         self.name = name
# # # #         self.salary = salary
# # # #         self.id_no = id_no
# # # #         self.job_role = job_role
# # # #         self.joining_date = joining_date


# # # # print(employee_1.name)
# # # # print(employee_1.salary)
# # # # print(employee_1.id_no)
# # # # print(employee_1.job_role)
# # # # print(employee_1.joining_date)

# # # class Employee:
# # #     #class attribute
# # #     age = 10
# # #     def __init__(self, name, salary, id_no, job_role, joining_date):
# # #         self.name = name
# # #         self.salary = salary
# # #         self.id_no = id_no
# # #         self.job_role = job_role
# # #         self.joining_date = joining_date

# # #     def display_details(self):
# # #         print(self.name,self.salary,self.id_no,self.job_role,self.joining_date)



# # # employee_1 = Employee("Aswin", 25000, 101, "Developer", "01-11-2026")
# # # employee_1.display_details()
# # # # Accessing class attribute
# # # print(Employee.age)

# # # #*******************************************#
# # # class Student:
# # #     count = 0
# # #     def __init__(self,name,age,height):
# # #         self.name = name
# # #         self.age = age
# # #         self.height = height
# # #         # increment count by 1, when class has initialized
# # #         Student.count=Student.count+1

# # #     #def display_count(self):
# # #      #   print(Student.count)

# # # #student_1 = Student("geethu",22,170)
# # # #student_1.display_count()

# # # class animal:
# # #     def __init__(self, has_leg):
# # #         self.has_leg = has_leg

# # # class Dog(animal):
# # #     pass

# # # dog = Dog(has_leg="yes")
# # # print("The dog has 4 leg",dog.has_leg)  # oru attribute nne verethilk kond varn
# # # #*****************************************************************#
# # # # 
# # # class Animals:
# # #     def __init__(self,sleep,eat,speaks):
# # #         self.sleep = sleep
# # #         self.eat= eat

# # # class Dog(Animals):
# # #     def __init__(self,sleep,eat, speaks):
# # #         super().__init__(sleep,eat,speaks)
# # #         self.speaks =speaks

# # # class Cat(Animals):
# # #     def __init__(self, sleep, eat,speaks):
# # #         super().__init__(sleep,eat,speaks)
# # #         self.speaks =speaks



# # # cat = Cat(speaks="yes",sleep="yes",eat ="yes")
# # # print("the cat can speaks",cat.speaks)
# # # dog = Dog(speaks="no",eat = "yes",sleep ="yes")
# # # print("the dog can't speaks",dog.speaks)

# # #******************************************#
# # class Animals:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age

# #     def eat (self):
# #         return "The Animals is eating"
        
# # class Dog(Animals):
# #         def bark(self, ):
# #             print("woof")

# # class Cat(Animals):
# #         def meow(self):
# #             print("meow")
# #             return "meow"
        
# # Cat = Cat("nim",21)
# # print(Cat.name,Cat.age,Cat.meow(),Cat.eat())

# # #*************************************************#
    
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age= age
#     def display(self):
#         print(self.name)
#         print(self.age) 

# class Student(Person):
#     def __init__(self, name, age,course):
#         super().__init__(self,name,age,course)  
#         self.course = course  

#     def showcourse(self):
#         print(self.course)

#         Person = person("")
        



from abc import ABC,abstractmethod

class bank(ABC):
    @abstractmethod
    def desposit(self):
        pass
    
   # @abstractmethod
    #def loan(self):
      #  pass   

class SBI(bank):
        #def deposit(self):
            #print("Deposit is excuted")

        def profit(self):
             print("profit")

        def loan(self):
            print("loan is applied")
#sbi = SBI()
#sbi.deposit()
#sbi.lon()

#*************************************************#
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Rectangle(Shape):

    def __int__(self,length,width):

        self.length = length
        self.width = width
        print(length*width)
    
    def area(self):
        return self.length,self.width
        

class Circle(Shape):
    def __int__(self,radius):

        self.radius=radius
        print(3.14*radius*radius)
    def area(self):
        return self.radius 

    
rectangle=Rectangle(5,4)
circle=Circle(2.5)
print(rectangle.area())
    
     
     
