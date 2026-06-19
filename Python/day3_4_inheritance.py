# """ OOPS inheritance """
# class Student:
#     """base class of inheritance"""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         """display method of base class"""
#         print(f"{self.name}: (Age: {self.age}, Degree: 'Not mentioned')")

#     def __str__(self):
#         return f"Student(Name: {self.name}, Age: {self.age})"

# class GraduateStudent(Student):
#     """"derived class of inheritance"""
#     def __init__(self, name, age, degree):
#         super().__init__(name, age)
#         self.degree = degree

#     def display(self):
#         """method of derived class"""
#         print(f"{self.name}: (Age: {self.age}, Degree: {self.degree})")

# student_1 = GraduateStudent("Alice", 25, "Bachelor's")
# student_1.display()

class BankAccount:
    """ base class of inheritance """
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """ method of base class """
        try:
            amount = float(amount)
            if amount <= 0:
                print("Deposit amount must be positive.")
                return
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        except TypeError:
            print("Invalid input. Please enter a numeric value for the deposit amount.")
        finally:
            print("Deposit operation completed.")

    def withdraw(self, amount):
        """method of base class"""
        try:
            amount = float(amount)
            if amount <= 0:
                print("withdrawal amount must be positive.")
                return
            if amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= amount
                print(f"Withdrawn {amount}. New balance: {self.balance}")
        # except TypeError:
        #     print("Invalid input. Please enter a numeric value for the withdrawal amount.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the withdrawal amount.")
        finally:
            print("Withdrawal process completed.")

    def __str__(self):
        return f"BankAccount(Owner: {self.owner}, Balance: {self.balance})"

class SavingsAccount(BankAccount):
    """ derived class of inheritance """
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """ method of derived class """
        print(f"Previous balance: {self.balance}")
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest: {interest}. New balance: {self.balance}")

    def __str__(self):
        return f"SavingsAccount(Owner: {self.owner}, Balance: {self.balance}, Interest Rate: {self.interest_rate})"

obj_1 = BankAccount("Punj", 1000)
obj_1.deposit(500)
obj_1.withdraw(200)
obj_1.withdraw(5000)
obj_1.withdraw("hello")
print(obj_1)
