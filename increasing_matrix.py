n, m = map(int, input().split())
# You can access the j-th element in the i-th row of matrix A using a[i][j].
# Works the same for B. Just make sure 0 <= j < n and 0 <= i < m.

a = [[int(val) for val in input().split()] for _ in range(n)]
b = [[int(val) for val in input().split()] for _ in range(n)]
i = 0 
j = 0
c = 'Possible'
x= 0
for i in range(n):
	for j in range(m):
# while x < m and y < n:
		if (i-1 >= 0):
			if a[i][j] <= a[i-1][j] or b[i][j] <= b[i-1][j]:
				x = a[i][j]
				a[i][j] = b[i][j]
				b[i][j] = x
				
				if a[i][j] <= a[i-1][j] or b[i][j] <= b[i-1][j]:
					c = 'Impossible'
# while x< m and y< n: 	
		if (j-1 >= 0):
			if a[i][j] <= a[i][j-1] or b[i][j] <= b[i][j-1]:
				x = a[i][j]
				a[i][j] = b[i][j]
				b[i][j] = x
				
				if a[i][j] <= a[i][j-1] or b[i][j] <= b[i][j-1]:
					c = 'Impossible'


print(c)
		
