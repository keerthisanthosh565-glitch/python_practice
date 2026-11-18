# class BankAccount:

    # def __init__(self, owner_name, bank_balance, account_type):
    #     self.owner_name = owner_name
    #     self.__bank_balance = bank_balance
    #     self._account_type = account_type

    # To get the private attribute
    # @property
    #def bank_balance(self):
        # return self.__bank_balance

    # To update the private attribute
    # @bank_balance.setter
    # def bank_balance(self, deposit_amt):
    #     if deposit_amt <= 0:
    #         raise ValueError("Deposit amount cannot be zero or negative")

    #     self.__bank_balance = self.__bank_balance + deposit_amt

    # To get account type
    # @property
    # def account_type(self):
        # return self._account_type

    # To update account type
    # @account_type.setter
    # def account_type(self, acc_type):
    #     if acc_type == "":
    #         raise ValueError("Account type cannot be empty")

        # self._account_type = acc_type


# bank = BankAccount("santhosh", 12000, "savings")

# print(bank.bank_balance)
# print(bank.account_type)

# bank.bank_balance = 123
# print(bank.bank_balance)

# bank.account_type = "current"
# print(bank.account_type)

#*******************************************#
class Employee:
    def ___init__(self,employee_name,department,salary):
        self.employee_name = employee_name
        self.department = department
        self.salary = salary

    # to get private attribute
    @property
    def salary (self):
        return self.salary

    # to get update salary
    @salary.setter
    def salary(self,salary):
        if salary=="":
            raise ValueError ("salary cannot be negative")


class Manager(Employee):
    def display_details(self):
        print(self.employee_name,self.department)
    @property
    def department(self):
        return self.department
# manager = Manager("keerthi","Data analystic",20000)
# manager.display_details()






#
class Vehicle:
    def ___init__(self,vehicle_name,_rental_type,__rental_price):
        self.vehicle_name = vehicle_name
        self._rental_type = _rental_type
        self.__rental_price = __rental_price

    # to get private attribute
    @property
    def rental_price (self):
        return self.rental_price

    @rental_price.setter
    def rental_price(self,rental_price):
        if rental_price=="":
            raise ValueError("rental price cannot be negative")
    def display_details(self):
        print(self.vehicle_name)
        print(self.rental_price)

#B
class Car(Vehicle):
    def calculate_rent(self,days):
        self.day= day
        print("total rental cost",self.rental_price*self.days)

    def display_details(self):
        print(self.vehicle_name)
        print(self.rental_type)
        print(self.rental_price)

class Bike(Vehicle,Car):
    def calculate_rent(self,day):
        self.day = day
        print("total rental cost",self.rental_price*self.day)

    def display_details(self):
        print(self.vehicle_name)
        print(self.rental_price)
        print(self.rental_type)


#C
car = Car("honda","4 wheeler",2000)
bike = Bike ("suzuki","2 wheeler",800)

car = Car.rental_price=2000
print(car.rental_price)
bike= Bike.rental_price=800
print(bike.rental_price)
#************************************#



 




        


