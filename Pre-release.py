# Task 1.6
def Staff_role(salary):
    if salary < 50:
        return "Assign Manager"
    elif salary >= 50 and salary < 70:
        return "Assign Lead Developer"
    elif salary >= 70 and salary < 90:
        return "Consultant"
    elif salary >= 90:
        return "Assign Project Manager"

# Task 2.3 & 2.5
class Toy:  # Base class

    # Constructor
    def __init__(self, Name, Identity, Price, Minimum_age):
        
        self.__Name = str(Name)
        
        if len(Identity) == 5:
            self.__Identity = Identity
        else:
            print("Identity should be 5 charaters long")
        
        self.__Price = Price
        
        try:
            self.__Minimum_age = int(Minimum_age)
        except ValueError:
            print("Minimum age must be integer")

    # Get Methods
    def get_Name(self):
        return self.__Name
    def get_Identity(self):
        return self.__Identity
    def get_Price(self):
        return self.__Price
    def get_Minimum_age(self):
        return self.__Minimum_age

    # Set Methods
    def set_Name(self, new_Name):
        self.__Name = new_Name
    def set_Identity(self, new_Identity):
        if len(Identity) == 5:
            self.__Identity = new_Identity
        else:
            print("Identity should be 5 charaters long")
    def set_Price(self, new_Price):
        self.__Price = new_Price
    def set_Minimun_age(self, new_Minimum_age):
        try:
            self.__Minimum_age = int(Minimum_age)
        except ValueError:
            print("Minimum age must be integer")
            
# Task 2.4
class ComputerGame(Toy): # Derived Class from 'Toy'

    # Constructor
    def __init__(self, Name, Identity, Price, Minimum_age, Category, Console):
        Toy.__init__(self, Name, Identity, Price, Minimum_age) # Inheritance
        self.__Category = Category
        self.__Console = Console

    # Get Methods
    def get_Category(self):
        return self.__Category
    def get_Console(self):
        return self.__Console

    # Set Methods
    def set_Category(self, new_Category):
        self.__Category = new_Category
    def set_Console(self, new_Console):
        self.__Console = new_Console

class Vehicle(Toy): # Derived Class from 'Toy'

    # Constructor
    def __init__(self, Name, Identity, Price, Minimum_age, Type, Height, Length, Weight):
        Toy.__init__(self, Name, Identity, Price, Minimum_age) # Inheritance
        self.__Type = Type
        self.__Height = Height
        self.__Length = Length
        self.__Weight = Weight

    # Get Methods
    def get_Type(self):
        return self.__Type
    def get_Height(self):
        return self.__Height
    def get_Length(self):
        return self.__Length
    def get_Weigth(self):
        return self.__Weigth

    # Set Methods
    def set_Type(self, new_Type):
        self.__Type = new_Type
    def set_Height(self, new_Height):
        self.__Height = new_Height
    def set_Length(self, new_Lenght):
        self.__Length = new_Length
    def set_Weight(self, new_Weight):
        self.__Weight = new_Weigth
        
# Task 2.6
objects = list()

# Creating Instance
car = Vehicle("Red Sports Car", "RSC13", 15, 6, "Car", 3.3, 12.1, 0.08)
game = ComputerGame("Forza Horizon 3", "FHZ03", 46.99, 0, "Racing", "Xbox One")

objects.append(car)
objects.append(game)

# Task 2.7
def Details(ID):
    for obj in objects:
        if obj.get_Identity() == ID:
            print(" Name = {0} \n ID = {1}".format(obj.get_Name(), obj.get_Identity()))
            print(" Price = {0} \n Minimun age = {1}".format(obj.get_Price(), obj.get_Minimum_age()))

# Task 2.8
def Discount(percentage):
    for obj in objects:
        old_price = obj.get_Price()
        new_price = old_price * (1 - percentage/100)
        obj.set_Price(new_price)

# Task 2.10
def Bubble_sort(array):
    if len(array) == 1:
        return
    
    flag = True
    while flag:
        flag = True
        for i in range(0, len(array)):
            if array[i].get_Price() > array[i+1].get_Price():
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                flag = False

def Insertion_sort(array):
    if len(array) == 1:
        return

    for i in range(1, len(array)):
        temp = array[i]
        position = i
        while array[position-1] > temp and position > 0:
            array[position] = array[position-1]
            position = position - 1
        array[position] = temp

# Task 3.1
"""
charater(habib) # do not start with capital letter
animal(fish)
skill(time travel)

charater_type(habib, explorer)
has_skill(habib, time travel)
pet(habib, fish)
"""

# Task 3.2
"""
pet(X, Y) if charater(X) and animal(Y) # capital letter means vriable
"""

# Task 3.4
"""
1. true
2. princess
3. jim
4. invisibility
5. jim
"""

# Task 3.5
"""
1. pet(jim, X)
2. has_skill(X, fly)
3. skill(X)
4. pet(charater_type(X, princess), Y)
"""
