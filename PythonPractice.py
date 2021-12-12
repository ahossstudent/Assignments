#1
def beeronwall(x):
	while x >= 1: 
		print(x, "bottles of beer on the wall, take one down, pass it around")
		x -= 1
	print("No bottles of beer on the wall")


#2
def factorial(x):
    result = 1
    test = 1
    for i in range(1, x + 1):
    	print(x,"*",test, "=", result)
    	test = x * result
    	result = result * x
    	x -= 1	
    return result

factorial(5)


#3
seconds = int(input("Enter number of seconds"))
choice = input("What should the number be converted to? Use all lower cases")


def change(a, b):
	if b == "minutes":
		convert = a/60
		print("This is", "{:.2f}".format(convert), b)
	elif b == "hours" :
		convert = a/3600 
		print("This is", "{:.2f}".format(convert), b)
	elif b == "days":
		convert = a/86400 
		print("This is", "{:.2f}".format(convert), b)
	else:
		convert = a/604800
		print("This is", "{:.2f}".format(convert), b)


#4
inventory = input("What type of inventory do you want to check? (Heads or Legs) Input exactly how listed")
if inventory == "Heads":
	chickens = int(input("Please enter the amount of chickens"))
	chickens_leg = chickens * 2 
	cows = int(input("Please enter the amount of cows"))
	cows_leg = cows * 4 
	print("We have", chickens, "chickens with a total of", chickens_leg)
	print("We have", cows, "cows with a total of", cows_leg)
elif inventory == "Legs":
	chicken_legs = int(input("Please enter the amount of chickens legs")) 
	while chicken_legs%2 != 0 :
		print("please enter again")
		chicken_legs = int(input("Please enter the amount of chickens legs"))
	chick = chicken_legs/2	
	print("We have", chick, "chickens")	
	cows = int(input("Please enter the amount of cows"))
	while cows%4 != 0 or cows < 4: 
		print("please enter again")
		cows = int(input("Please enter the amount of cows"))
	cowcount = 	cows/4
	print("We have", cowcount, "cows")
    
    
    
 #5
for i in range(1, 10 + 1):
    print(" ")
    for j in range(1, 10 + 1):
        if(i % 2 != 0): 
            print('1', end = "\t")
            i += 1
        else:
            print('0', end = "\t")
            i += 1
    print()   