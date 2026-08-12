num = [1,2,3,4,5]
print(num)  

print("First element:", num[0] )
print("Last element: ", num[-1])

num[2] = 35
print("changing index 2: \n", num)

print("First three elements: ", num[0:3])
print("Every second element: ", num[::2])
print("Reversed list: ", num[::-1])


sqr = [x**2 for x in num]
print("\nList Comprehensions...")
print("square of list: ", sqr)
