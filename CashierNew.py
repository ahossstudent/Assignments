def calculate_change(x):
    if payment_method == "CASH":
        cash = float(input("How much are you paying in cash"))
        if cash > item_price_total:
            change = cash - item_price_total
            print("You gave us",cash, " and we owe you", "{:.2f}".format(change), " Thank you for your purchase")
        elif cash == item_price_total:  
            print("Thank you for your purchase")
        else:
            print("You have not paid the full amount. Your items will be returned to the shelves. Thank you!")  
    elif payment_method == "CREDIT": 
        print("You are getting charged", "{:.2f}".format(item_price_total), "Thank you for your purchase")

    else:
        print("You didn't enter CASH or CREDIT")

checkouttype = input("Express Checkout or Regular? Please enter exactly how it is displayed (Express or Regualar)?")
print("WELCOME!")
if checkouttype == "Express":
    i = 1
    item_price_total = 0.00
    summary = ""
    cust = 'Y'
    while i < 6 and (cust == 'Y' or cust == 'y'):
        item_new = input("What is your item?")
        item_price = float(input("How much does it cost? "))
        item_qty = int(input("How many are you purchasing?"))
        item_total = item_price * item_qty
        summary += str(item_new)+"\t\t"+str(item_total)+"\n"
        item_price_total += item_total
        i += 1
        cust = input("Do you want to add another item? Y/N")
        
    print("\nItem\tCost")
    print(summary)

    print("Your total is", "{:.2f}".format(item_price_total))

    payment_method = input("How are you paying? CASH OR CREDIT. Please enter all capital letters with no spaces")
    calculate_change(payment_method)
elif checkouttype == "Regular":  
    i = 1
    item_price_total = 0.00
    cust = 'Y'
    while cust == 'Y' or cust == 'y':
        item_new = input("What is your item?")
        item_price = float(input("How much does it cost? "))
        item_qty = int(input("How many are you purchasing?"))
        item_total = item_price * item_qty
        item_price_total += item_total
        i += 1
        cust = input("Do you want to add another item? Y/N")
        print("You are purchasing ", item_qty, item_new, "for ", item_price, "each")

    print("Your total is", "{:.2f}".format(item_total))
    payment_method = input("How are you paying? CASH OR CREDIT. Please enter all capital letters with no spaces")
    calculate_change(payment_method)