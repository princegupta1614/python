name = "Marvadi"

print("Updating one character of String: ", name, id(name))
try:
    name[3] = "w"
except Exception as e:
    print(e)


x = (10, 20, 30)

print("\nUpdating item of tuple: ", x)
try:
    x[1] = 25
except Exception as e:
    print(e)


print("\nPrevious id of x: ", id(x))
print("Value of x: ", x)
x = (1,2,3,4,5)
print("Updated id of x: ", id(x))
print("Value of x: ", x)
