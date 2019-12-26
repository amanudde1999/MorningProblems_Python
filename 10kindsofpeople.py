# read the input

n,m = (input().split())
n = int(n)
m = int(m)
a=[]
binary = input()

for numbers in range(m):
	i,j = input().split()
	i = int(i)
	j = int(j)
	if binary.find('0',i-1,j) != -1 and binary.find('1',i-1,j) != -1:
		a.append('both')
	if binary.find('0',i-1,j) == -1 and binary.find('1',i-1,j) != -1:
		a.append('one')
	if binary.find('0',i-1,j) != -1 and binary.find('1',i-1,j) == -1:
		a.append('zero')
for elements in a:
	print(elements)

# solve the problem

# output the answer
