lists = input().split()
dictionary = dict()
final  = []
for elements in lists:
	dictionary[elements] = lists.count(elements)
maximum = max(dictionary.values())

for i in dictionary.keys():
	if dictionary[i]== maximum:
		final.append(i)

final.sort()

for words in final:
	print(words)