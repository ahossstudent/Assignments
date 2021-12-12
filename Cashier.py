print("""My name is Ahmmed
I am from Brooklyn 
My favorite color is Green
My favorite sport is basketball""")

first_item = input("Welcome. What is your first item? ")

first_item_price = input("How much does it cost? ")
first_item_qty = float(input("How many are you purchasing"))

second_item = input("What is your second item? ")

second_item_price = input("How much is it? ")
second_item_qty = float(input("How many are you purchasing"))

third_item = input("What is your last item? ")

third_item_price = input("How much is it? ")
third_item_qty = float(input("How many are you purchasing"))

sumprice = (float(first_item_price) * first_item_qty) + (float(second_item_price) * second_item_qty) + (float(third_item_price) * third_item_qty)

print(first_item, "-", first_item_price, "and you are purchasing", "{:.0f}".format(first_item_qty))
print(second_item, "-", second_item_price, "and you are purchasing", "{:.0f}".format(second_item_qty))
print(third_item, "-", third_item_price, "and you are purchasing", "{:.0f}".format(third_item_qty))
print("Total - ", "{:.2f}".format(sumprice))

payment_method = input("How are you paying? CASH OR CREDIT. Please enter all capital letters with no spaces")

if payment_method == "CASH":
        cash = float(input("How much are you paying in cash"))
        if cash > sumprice:
            change = cash - sumprice
            print("You gave us",cash, " and we owe you", "{:.2f}".format(change), " Thank you for your purchase")
        elif cash == sumprice:	
            print("Thank you for your purchase")
        else:
            print("You have not paid the full amount. Your items will be returned to the shelves. Thank you!")	
elif payment_method == "CREDIT": 
        print("You are getting charged", "{:.2f}".format(sumprice), "Thank you for your purchase")

else:
		print("You didn't enter CASH or CREDIT")