def Introduction():
    print("Welcome, what company are you from and how much fiber optic would you like ")    
    
    
def Main():
    company = input('Company name: ')  #Cx inputs company name
    length = input('amount of fiber optic wires in feet: ') #Cx inputs required amount of cable
    cost = .87 
    total = float(length)*float(cost)  #cost calculation for amount of cables Cx inputed
    print(company,"cost total for", length, "feet is: $",total) #informs Cx the total cost

Introduction()
Main()