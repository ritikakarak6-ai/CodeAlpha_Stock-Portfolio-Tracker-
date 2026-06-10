stk = {"AAPL": 180, "TSLA": 250, "MSFT": 400}

print("We have limited stocks and their prices:")
print("1. AAPL: 180\n2. TSLA: 250\n3. MSFT: 400")

a = input("\nWhich company's stock have you bought? (AAPL/TSLA/MSFT): ").upper() # Automatically converts to uppercase
b = int(input("How many stocks have you bought?: "))

if a in stk:
    per_stock_price = stk[a]
    total_cost = per_stock_price * b
    
    print("\n------Your investment summary------")
    print("Stock name:                  ", a)
    print("Quantity of stock purchased: ", b)
    print("Price per stock:             ", per_stock_price)
    print("Total Investment:            ", total_cost)
    
    save = input("\nDo you want to save the result in a file (yes/no)? ").lower()
    
    if save == "yes":
        try:
            with open("portfolio.txt", 'w') as file:
                file.write("------Your investment summary------\n")
                file.write(f"Stock name: {a}\n")
                file.write(f"Quantity of stock purchased: {b}\n")
                file.write(f"Price per stock: {per_stock_price}\n")
                file.write(f"Total Investment: {total_cost}\n")
                file.write("------------------------------------------")
            print("Success! Your portfolio has been saved in 'portfolio.txt'.")
            
        except PermissionError:
            print("\n[Permission Error] Could not save the file.")
            print("Reason: If you are using an online compiler, it might restrict file saving.")
            print("If running locally, make sure 'portfolio.txt' isn't already open in another app.")
    else:
        print("Result not saved.")
        
else:
    print("Please enter a valid stock from the limited stock options...")
