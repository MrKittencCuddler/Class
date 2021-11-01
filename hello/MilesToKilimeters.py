#Gabe Poppen // introduction to Programming
# Miles to kilimeters calcuator 
def Unit():
    miles = (input("Enter a distance in miles: "))
    
    try:
        miles = float(miles)    #Checks if miles entered is a number
    except:
        print("Mile input is not accepted") #error message
        Unit()      #loops Unit funtion
    else:
        Calculations(miles)

def Calculations(miles):    #calculating how many kilometers
    
    converstion = 1.609     #conversion factor
    kilimeters = miles*converstion      #conversion math
    output(kilimeters,miles)

def output(kilimeters,miles):
    print("original milage is",miles, "while in kilimeters, it is" ,kilimeters)     #output message

def main():
    print("This program will convert miles to kilimeters")      #introduction
    Unit()
main()