
# read in the input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = x2 - x1
b = x4 - x3
if (x2-x1) != 0 and (x4-x3) != 0:
	slope_1 = (y2-y1)/(x2-x1)
	#abs(slope_1)
	slope_2 = (y4-y3)/(x4-x3)
	#abs(slope_2)
	if slope_1-slope_2 == 0:
		print('parallel')
	else:
		print('not parallel')
else:
	print('parallel')
# now solve the problem. good luck :D