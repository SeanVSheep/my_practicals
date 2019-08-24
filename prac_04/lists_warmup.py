numbers = [3, 1, 4, 1, 5, 9, 2]
'''
numbers[0] = 3
numbers[-1] = 2
numbers[3] = 1
numbers[:-1] = [3, 1, 4, 1, 5, 9]
numbers[3:4] = [1, 5] WRONG THIS = [1]
5 in numbers = True
7 in numbers = False
"3" in numbers = False
numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
'''

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])

#Q1-  Change the first element of numbers to "ten"
numbers[0] = "ten"
print(numbers)

#Q2- Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

#Q3-  Get all the elements from numbers except the first two
print(numbers[2:])


#Q4-  Check if 9 is an element of numbers
print("9 is in numbers: {}".format(9 in numbers))


