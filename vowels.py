# read the input
string = input('')
# solve the problem
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0

for letters in string:
	if letters in vowels:
		count=count+1
	

# output the result
print(count)
