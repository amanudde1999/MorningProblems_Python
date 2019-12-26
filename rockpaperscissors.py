Bob_wins = ['RP','SR','PS']
Alice_wins = ['PR','RS','SP']
Tie = ['SS','PP','RR']

alice_wins_rounds = 0
bob_wins_rounds = 0
bob_wins_matches = 0
alice_wins_matches = 0
#i = 0
tie = 0
idc = 0
num_matches = int(input())
for i in range(num_matches):
	matches = []
	matches = input().split()
	#number_of_rounds = len(what)
	bob_wins_rounds = 0
	alice_wins_rounds = 0 
	for elements in matches:
		if elements in Bob_wins:
			bob_wins_rounds +=1
		elif elements in Alice_wins:
			alice_wins_rounds += 1
		elif elements in Tie:
			tie +=1
	if bob_wins_rounds > alice_wins_rounds:
		bob_wins_matches += 1		
	elif bob_wins_rounds < alice_wins_rounds:
		alice_wins_matches +=1
	elif bob_wins_rounds == alice_wins_rounds:
		idc += 1

if alice_wins_matches < bob_wins_matches:
	print('Bob', bob_wins_matches)
elif alice_wins_matches > bob_wins_matches: 
	print('Alice', alice_wins_matches)
elif alice_wins_matches == bob_wins_matches:
	print('Alice', alice_wins_matches)

