'''
Author: Braden DeForest
Program: Car Data
Original File Name: cardata.py
Description:
    This will take user data on a car, and output it in an easy to read format.
Usage:
    python cardata.py
Command Line Arguments:
    None
'''

# Create a superclass called vehicle.
class Vehicle:
    '''Abstract class for vehicle.'''
    type = ""

# Create a class that extends vehicle
class Automobile(Vehicle):
    '''Extends Vehicle.'''
    year = 0    # This needs to be int
    make = ""   #str
    model = ""  #str
    doors = 0   #int, can either be 0, 2, or 4 
    roof = ""   #str


# Get input for a car.
theCar = Automobile() # A class to hold the data
theCar.type = "car" #Because its a car, so theres no other option.
while True:
    try: #String to int conversion... yay...
        theCar.year = (int(input("What is the year? ")))
        break
    except:
        print("Invalid year. Please type a year in the form XXXX")
theCar.make = input("What is the make? ")
theCar.model = input("What is the model? ")
while True:
    try: #Another conversion...
        theCar.doors = (int(input("How many doors are there? ")))
        break
    except:
        print("Invalid number of doors.")
theCar.roof = input("Is the roof solid or a sun roof? ")

# Now that we have it all, lets print it.
print("\n--------------Data--------------")
print("Vehicle type:", theCar.type)
print("Year:", theCar.year)
print("Make:", theCar.make)
print("Model:", theCar.model)
print("Number of doors:", theCar.doors)
print("Type of roof:", theCar.roof)