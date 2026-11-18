class Person:
    def __init__(self,name,age):
        self.name = name
        self.age= age

    def display_detail(self):
        print(f"name is{self.name} and age: {self.age}")

class Employee(Person):
    def __init__ (self,name, age, emp_id,salary,joining_date):
       super().__init__(name,age)
       self.emp_id = emp_id
       self.salary = salary
       self.joining_date = joining_date


    def display_detail(self):
        print(f"name is{self.name}and age:{self.age},and emp_id:{self.emp_id},and salary:{self.salary},and joining_date:{self.joining_date}")


class Father(Person):
    def __init__(self,name,age,no_of_childern):
        super().__init__(self,name,age,no_of_childern)
        self.name = name
        self.age = age
        self.no_of_childern = self.no_of_childern

    def display_detail(self):
        print(f"name is {self.name} and age:{self.age} and children {self.no_of_childern}")


class Son(Person):
    def __init__(self, name, age,father_name):
        super().__init__(self,name,age)
        self.father_name = father_name

    def display_detail(self):
        print(f"name is{self.name} and age:{self.age} father name is {self.father_name}")

class Husband(Person):   
    def __init__(self, name, age,wife_name,date_marriage):
        super().__init__(name, age,)
        self.wife_name = wife_name
        self.date_marriage = date_marriage

        def display_detail(self):
            print(f"name is {self.name}and age:{self.age}and wife name:{self.wife_name} and date_marriage:{self.date_marriage}")


          

person = Person("santhosh", 45)
person.display_detail()

employee = Employee("santhosh",45,101,25000,"11/1/2024")
employee.display_detail()


#**********************************************************************#

#
class BankAccount:
    def __init__(self,account_holder,_account_type, balance):
        self.account_holder = account_holder
        self._account_type = _account_type
        self.__balance = balance
#getter
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        if amount <= 0:
            print("balance cannot be negative")
            self.balance= amount

    def deposit(self,amount):
         if amount >0:
              self.balance= self.balance + amount
              print("deposit:"amount)
        
class SavingsAccount(BankAccount):
    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def __init__(self, account_holder,  balance):
        super().__init__(account_holder,  balance)()
    def account_type(self,account_tpe): 
        if account_tpe == "savings":
    def calculate_interest(self):
        return self.balance*0.05
        


    class CurrentAccount(BankAccount):
    def _account_type(self):
            return self._account_type

     @account_type.setter
    def account_type(self,account_holder,balance):
            super().__init__(account_holder,balance)
    def account_type(self,account_type):
            if account_type =="current":
    def calculate_interest(self):
            return self.balance*0.02

    #creating Account
     
    