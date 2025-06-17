'''
Name: Braden DeForest
Original file name: mod2lab.py

Description:
    This will take student's name and GPA and tell the user whether they
    qualify for Dean's List or Honor Roll.

Syntax:
    python ./mod2lab.py
Arguments:
    None
'''

# Variables
studentName = ""
gpa = 0.0

#For user friendliness
print("\nUser Search\n")

#Inputs
while True:
    studentLastName = input("Type the student's last name (\"ZZZ\" to quit): ")
    if studentLastName == "ZZZ" or studentLastName == "zzz":
        print("Processing canceled.")
        break
    studentFirstName = input("Type the student's first name: ")
    while True: #Why a whole function for this?? Well, this is where people are
                #almost certainly going to have an error. May as well stop it!
        gpaTemp = input("What is the GPA? ")
        try:
            gpa = float(gpaTemp)
            if gpa > 5:
                print("Please give a valid GPA.\n")
                continue
            break
        except:
            print("Error: Please type a valid number.\n")
            
    print("\nUsing \"" + studentLastName + " " + studentFirstName + ": " + \
          str(gpa) + "\":\n")

    # Calculation time...
    if gpa >= 3.5:
        print("\tStudent it on Dean's List.")
        print("\tStudent is on Honor Roll.\n")
    elif gpa >= 3.25:
        print("\tStudent is on Honor Roll.\n")
    else:
        print("\tStudent is not on Dean's List or Honor Roll.\n")

print("Closing program.")
exit(0) #Just to make sure 0 is used.