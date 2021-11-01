def Introduction():
    print("Welcome, what company are you from and how much fiber optic would you like ")    
    
    
def Company_Calculations():
    company = input('Company name: ')  #Cx inputs company name
    length = int(input('amount of fiber optic wires in feet: ')) #Cx inputs required amount of cable
    cost = 0
    if length <= 100:   # if length is 100ft or under than cost is .87
        cost = .87
    elif length <= 250:     # if length is between 100ft and 250ft than cost is .80
        cost = .80
    elif length <= 500:     # if length is between 250ft and 500ft than cost is .70
        cost = .70
    elif length > 500:     # if length is 500ft or over than cost is .50
        cost = .50 
    total = float(length)*float(cost)  #cost calculation for amount of cables Cx inputed
    print(company,"cost total for", length, "feet is: $",total) #informs Cx the total cost

Introduction()
Company_Calculations()