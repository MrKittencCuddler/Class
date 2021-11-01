# Gabe Poppen
#Intro to Programming 
#!.usr/bin/env python
def intro(): #INTRODUCTION STUFF
    print("Program will check check these stocks: AAPL, AMZN, BTCUSD, COMP, DJIA, ETHUSD, GOOG, MSFT, SPX, TSLA")  #stock list
    print("and display the value of the choosen stock")
    print("It is case sensitive, do it in all CAPS")

def dictionary(): #Will make a dictionary list of the stocks stated above and call the stock value
    ticker = input("Enter the stock:")
    #dictionary list
    stock = {'AAPL': '$142.53', 'AMZN': '$3246.30', 'BTCUSD': '$57171.50', 'COMP': '$10.74', 'DJIA': '$34496.06', 'ETHUSD': '$3501.71',
    'GOOG': '$2776.95', 'MSFT': '$294.23', 'SPX': '$4361.91', 'TSLA': '$791.94'}
    if ticker in stock: # Checks if input is in the list provided
        print(ticker, "value is", stock[ticker].title())
    else:
        print("You miss-typed or did not choose a stock on the list")       #lol rejection
        dictionary()

def main():
    intro()
    dictionary()

main()
