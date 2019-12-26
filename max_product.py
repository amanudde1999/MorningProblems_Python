n = int(input())


x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.sort(reverse = True)
y.sort(reverse = True)
suma = 0
for i in range(0,n):
	suma = suma + (x[i]*y[i])
print(suma)

	 
