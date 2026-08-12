nums = [1,2,3,3,3,4,5,6,7]

list_sqr = [num ** 2 for num in nums]
set_sqr = { num ** 2 for num in nums}
dict_sqr = {num: num ** 2 for num in nums}

print("Original: ", nums)
print("List comprehension: ",list_sqr)
print("Set comprehension: ",set_sqr)
print("Dict comprehension: ",dict_sqr)
