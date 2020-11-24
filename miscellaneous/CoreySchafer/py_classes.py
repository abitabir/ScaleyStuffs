# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

# we want to represent our emplyees in our company in python
# we can do this by making a class template/blueprint employee for every individiual
#  employee in our company to be instantiated/created from
# each employee has similar categories of attributes they possess {properties} and methods they can perform {behaviours}

class Employee:
    pass

employee_1 = Employee()
# creating instance of class Employee called employee_1
# note: instance name is passed in automatically as first parameter in Employee() in this statement
# or any other instance creation statement
employee_2 = Employee()
# both are unique employee objects now that have been created

employee_1.firstname = "Muchu"
employee_1.lastname = "Mian"
employee_1.lastname = "Muchu.Mian@company.com"
employee_1.pay = 9000

employee_2.firstname = "Abir"
employee_2.lastname = "Riba"
employee_2.lastname = "Abir.Riba@company.com"
employee_2.pay = 9500
# but it isn't useful to manually set the attributes this wat - it's a lot of code and so prone to syntax errors XS

print(employee_1)
print(employee_2.email)

# say we want to have a method to print out the fullname of an employee
print("{} {}".format(employee_1.lastname, employee_1.firstname))
# but this is fiddly every timeeee XOS


# better implementation of Employee class, in which you set the attributes
# automatically when you create employee_n, using a special init method (initialised, or constructor, think of it as)

class Worker:

    # class variables are variables that are shared amongst each instance of the class
    # can update it {kinda like constants} everytime we wanna change it
    number_of_workers = 0
    annual_raise_by = 1.04


    def __init__(self, firstname, lastname, hours, pay):
        # in all methods within a class they recieve the instance as the first argument/parameter automatically
        # by convention this parameter is called self - don't use anyt else even if you can, 'tis bad practice
        # after self specify all the arguments that you want the instances of this class to accept
        # then, in body of method, add what you want to be the properties of the instance passed in the instance
        # creation parameters, to the instance as its properties
        # these are instance variables which are data that are unique to each instance
        self.firstname = firstname
        self.lastname = lastname
        self.hours = hours
        self.email = firstname + "." + lastname + "@company.com"
        self.pay = pay
        # using constant class value here, hum
        Worker.number_of_workers += 1

    def fullname(self):
        # works with all instances of Worker =)
        return "{} {}".format(self.lastname, self.firstname)

    def apply_raise(self):
        self.pay = int(self.pay * self.annual_raise_by)
        # could replace self.annual_raise with Worker.annual_raise, but former gives more flexibility
        # e.g if you want to give a certain worker more raise than others


worker_1 = Worker("Nazo", "Mad", "fulltime", 4325)
# more concise!
worker_2 = Worker("Rijju", "Paaray", "parttime", 3254)

print(worker_1.lastname)
print(worker_2.hours)

print(worker_2.fullname())
# above and below work the same way =0 ~ above turns into below in background, why self passed as parameter, hum
print(Employee.fullname(worker_1))

print(worker_1.pay)
worker_1.apply_raise()
print(worker_1.pay) # is incremented

# can access class variable raise_amount_by through all three, but latter two instances don't acc have the variable
# themselevs (you won't find it in the namespace of any of the instances
# (UNLESS you have changed the raise_amount_by variable of a particular instance to sommat different from the class var
# e.g by worker_2.raise_amount_by = 1.05 ) but you will in namespace of class
# note: you see namespace of instance worker_1 by: print(worker_1.__dict__)
# and you see namespace of class Worker by: print(Worker.__dict__))
# they are instead accessing the variable from the general class above them
Employee.raise_amount_by
worker_2.raise_amount_by
worker_1.raise_amount_by



# py inheritance ~ tutorial source https://www.youtube.com/watch?v=qiSCMNBIP2g

class A:

    def __init__(self):
        print("This is A's init")

    def feature1(self):
        print("Function 1 is working.")

    def feature2(self):
        print("Function 2 is working.")


class B(A):  # class B extends A, aka all the functions in A have been inherited by B and B can carry them out on top
    # of functions specific to B that are defined here in B - B is a child class, a subclass, but A's functionality is
    # a subset of B's functionality
    # this is single level inheritance

    def __init__(self):
        # super().__init__()  # if you want b1 = B() to print out A init as well as B init
        print("This is B's init")

    def feature4(self):
        print("Function 4 is working.")

    def feature3(self):
        print("Function 3 is working.")

a1 = A()  # prints out A init
b1 = B()  # prints out B init

class C:

    def __init__(self):
        print("Class C's init method is indeed working.")

    def feature5(self):
        print("Function 5 is working.")

    def feature6(self):
        print("Function 6 is working.")


class D:

    def __init__(self):
        print("Class D's init method is indeed working.")

    def feature8(self):
        print("Function 8 is working.")

    def feature7(self):
        print("Function 7 is working.")


class E(C, D):  # E is uniting C and D - this process is called multiple inheritance

    def __init__(self):
        super().__init__()  # which parent's initialiser do you think will be called? there should be no bias cuz they
        # are both equally the parents, but there is - only C's init method is called upon printation
        # however we have this concept called method resolution order (MRO) which always starts from left to right
        # so for the left super to be called is how it is
        print("Class C's init method is indeed working.")

    def feature9(self):
        print("Function 9 is working.")


print(E.feature6(), E.feature8())  # method feats from both parents of E can be called from E


# polymorphism ~ objects can have different forms (humans act differently in diffrent environments with different peeps)
# it is used in loose coupling processes, dependency injection, interfaces

# in python polymorphism can be carried out via duck typing, operator overloading, method overloading, method overriding
# you don't need to define what type is contained in a variable in python unlike java or c++
# if it looks like a duck, talks like a duck, behaves like a duck - we come to conclusion it is a duck. hum.
# if its behaviour is like something, it is that something - how to implement this in programming, hum

class Pycharm:

    def execute(self):
        print("Checking...")
        print("Debugging...")
        print("Compiling...")
        print("Executing...")


class MyEditor:

    def execute(self):
        print("Fetching...")
        print("Decoding...")
        print("Executing...")


class Laptop:

    def code(self, ide):
        ide.excecute()


ide1 = MyEditor()
ide2 = Pycharm()

lap1 = Laptop(ide1)
lap1 = Laptop(ide2)
# type of IDE is not fixed - it doens't matter which class object you are passing in through parameter, as long as that
# class has an execute method defined in it that can be called by the class Laptop
# this is duck typing

