
leftlane = input().split()
rightlane = input().split()
new_list = []
# now do something similar to get the list of vehicles in the right lane

minimum = min(len(leftlane),len(rightlane))
# For loop to iterate alternatingly over all the cars
for cars in range(minimum):
	alternate_left = leftlane.pop(0)
	alternate_right = rightlane.pop(0)
	alternate = (alternate_left,alternate_right)
	new_list.extend(alternate)

# Adding the rest of the cars that werent added in for loop
new_list.extend(leftlane)
new_list.extend(rightlane)


print(*new_list)

