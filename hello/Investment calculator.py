def introduction():
    print("This program calculates how long it takes for an investment to double in size.") #introduction message

def invest():
    investment = int(input("Enter your intial investment amount: "))     #cx sets inital investment value
    rate = int(input("Enter the annualized interest rate: "))            #cx sets intrest rate
    year = 0
    
    while investment != (investment*2):     #loop calculates till investment is doubled
        interest = (investment * rate * 1)/100 
        investment = investment + interest
        year += 1
    print("The number of years it takes for your investment to double is",year) #output for cx 

introduction()
invest()
