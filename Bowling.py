import random

players = []
i = 1
numberPlayers = int(input('How many players are going to Bowl?'))

while i <= numberPlayers:
	players.append(input('Enter Player name'))
	i += 1

def roll(): 
	first = random.randint(1, 10)
	if first == 10:
		second = 0
	if first != 10:
		test = 10 - first
		second = random.randint(1, test)
	return first, second

info = open('BOWLING.txt', 'w')
for i in range(1, 11):
	for x in range (numberPlayers):
		roll1, roll2 = roll()
		roll1 = str(roll1)
		roll2 = str(roll2)alrig
		print(players[x], roll1, roll2)
		info.write(players[x]+"\n")
		info.write(roll1+"\n")
		info.write(roll2+"\n")
info.close()



def calculateScore(name):
	f = open("BOWLING.txt", 'r')
	rows = f.read().splitlines()
	f.close()
	score=0
	count=0
	for row in rows[::3]:
		if row==name:
			score+=int(rows[count+1])+int(rows[count+2])
		count+=3
	return score



for x in players: 
	print("Name:", x, "Score:", calculateScore(x))

	
