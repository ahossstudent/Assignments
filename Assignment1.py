#Number 1 

text = open('Alone_EdgarAllenPoe.txt','r')
num_of_lines = 0
num_words = 0
number_of_characters = 0
space_count = 0
spaces = 0
newFileText = ""
nospacescount = 0

line = text.readline().rstrip()

while line!='':
	nospaces = len(line) - line.count(" ")
	words = line.split()
	num_words += len(words)
	number_of_characters += len(line)
	num_of_lines += 1
	spaces += spaces
	nospacescount += nospaces
	newFileText += line+"\n"
	line = text.readline().rstrip()
text.close()

print("The file has",num_of_lines, "lines")
print("The number of characters", nospacescount, "excluding spaces")
print("The number of", number_of_characters, "characters")

dash_char = (newFileText.count("--"))
without_dash = num_words - dash_char
print("The file has", without_dash, "words excluding dashes")



#Number 2

pigLatin = open("Alone_EdgarAllenPoe.txt", "r")
lineone = pigLatin.readline().rstrip()
split = lineone.split()
for Word in split:
    print(Word[1:] + Word[0] + "ay")
pigLatin.close()


#Number 3
import random 
newlist1 = []
newlist2 = []
newlist3 = []
first = random.randint(1,20)
second = random.randint(1,20)
third = random.randint(1,20)

for x in range(first):
	numbers = random.randint(1,100)
	newlist1.append(numbers)
sum1 = sum(newlist1)
avg1 = sum(newlist1) / first
range1 = max(newlist1) - min(newlist1)
print("List 1:", newlist1)
print("Sum of list one is", sum1)
print("Average:", avg1)
print("Range:", range1)
print()

for x in range(second):
	numbers = random.randint(1,100)
	newlist2.append(numbers)
sum2 = sum(newlist2)
avg2 = sum(newlist2) / second
range2 = max(newlist1) - min(newlist1)
print("List 2:", newlist2)
print("Sum of list one is", sum2)
print("Average:", avg2)
print("Range:", range2)
print()

for x in range(third):
	numbers = random.randint(1,100)
	newlist3.append(numbers)
sum2 = sum(newlist3)
avg2 = sum(newlist3) / third
range2 = max(newlist3) - min(newlist3)
print("List 1:", newlist3)
print("Sum of list one is", sum3)
print("Average:", avg3)
print("Range:", range3)
print()
