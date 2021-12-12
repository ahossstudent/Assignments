from collections import defaultdict

a_dictionary = {}
a_file = open("german.txt")

for line in a_file:
    key = line.rstrip()
    value = a_file.readline().rstrip()
    
    a_dictionary[key] = value

a_file.close()



b_dictionary = {}
b_file = open("french.txt")


for line in b_file:
    key = line.rstrip()
    value = b_file.readline().rstrip()
    
    b_dictionary[key] = value

b_file.close()



c_dictionary = {}
c_file = open("spanish.txt")

for line in c_file:
    key = line.rstrip()
    value = c_file.readline().rstrip()
    
    c_dictionary[key] = value

c_file.close()


dd = defaultdict(list)

for d in (a_dictionary, b_dictionary, c_dictionary): 
    for key, value in d.items():
        dd[key].append(value)

trans = input("Input what you would like translated")

if trans in dd:
    print(dd[trans])
else:
    print("Translations not found")

new_trans = 'Yes'

new_trans = input("Do you want to add something to the dictionary? (Yes or NO")

a_file = open("german.txt", 'a')
b_file = open("french.txt", 'a')
c_file = open("spanish.txt", 'a')

while new_trans == 'Yes':
	new_phrase = input("Please enter the phrase in english")
	a_file.write(new_phrase+"\n")
	b_file.write(new_phrase+"\n")
	c_file.write(new_phrase+"\n")
	french = input("Now enter it in french")
	b_file.write(french + "\n")
	german = input("Now enter it in german")
	a_file.write(german + "\n")
	spanish = input("Now enter it in spanish")
	c_file.write(spanish+"\n")


	new_trans = input("Do you want to add something else to the dictionary?")



a_file.close()
b_file.close()
c_file.close()