
# Read in the input
n = input()
n= int(n)
word_dict = dict()
for elements in range(n):
	binary,words = input().split()
	word_dict[binary] = words
binary_full = input()
length = len(binary_full)+1
i = 0
string = []

for elements in range(length):
	a = binary_full[i:elements]
	if a in word_dict:
		string.append(word_dict[a])
		i = elements 
		
print(*string,end = '')
print()
	