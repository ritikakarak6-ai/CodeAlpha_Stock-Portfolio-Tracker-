**Python Code **


stk={"AAPL": 180, "TSLA": 250, "MSFT":400}
print("We have limited stocks and their prices:", "\n1. AAPL: 180", "\n2. TSLA: 250", "\n3. MSFT: 400")
a=input("Which company's stock have you bought?(AAPL/TSLA/MSFT) :")
b=int(input("How many stocks have you bought? :"))
if a in stk:
    d=stk[a]
    c=d*b
    print("\n------Your investment summery------")
    print("Stock name: ", a)
    print("Quantity of stock purchased: ",b)
    print("The current price of each Stock: ", c)
    save=input("Do you want save the result in a file (yes/no)? ".lower())
    if save=="yes":
        try:
            with open("stk.txt", 'w') as file:
                file.write("------Your investment summery------\n")
                file.write(f"Stock name: {a}\n")
                file.write(f"Quantity of stock purchased: {b}\n ")
                file.write(f"The current price of each Stock:{c}\n")
                file.write("------------------------------------------")
            print("Success! Your portfolio has been saved in 'portfolio.txt'.")
        except PermissionError:
            print("\n[Permission Error] Could not save the file.")
            print("Reason: If you are using an online compiler, it might restrict file saving.")
            print("If running locally, make sure 'portfolio.txt' isn't already open in another app.")
    else:
        print("Result not saved" )
        
else:
    print("please! enter right stock in this limited stocks...")
    

    
