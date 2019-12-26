# Read the input
a, b, c = map(int, input().split())


# Solve the problem

avg = (a+b+c)/3 

x = int(abs(a-avg))
y = int(abs(b-avg))
z = int(abs(c-avg))
# Output the result
print(x,y,z)