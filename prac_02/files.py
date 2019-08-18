#1
name = input("Enter your name: ")
my_file = open('name', 'w')
my_file.write(name)
my_file.close()

#2
my_file = open('name', 'r')
'''
for line in my_file:
    print("Your name is", line.strip())
'''
name = my_file.read().strip()
print("Your name is", name)
my_file.close()

#3
numbers_file = open('numbers.txt', 'w')
numbers = (17, 42)
for i in range(len(numbers)):
    numbers_file.write(str(numbers[i]) + '\n')
numbers_file.close()

my_numbers = open('numbers.txt', 'r')
numbersTotal = 0
for line in my_numbers:
    numbersTotal += int(line)
print(numbersTotal)
my_numbers.close()

#4
numbers_file = open('numbers.txt', 'w')
numbers = (17, 42, 73, 123, 65, 2)
for i in range(len(numbers)):
    numbers_file.write(str(numbers[i]) + '\n')
numbers_file.close()

my_numbers = open('numbers.txt', 'r')
numbersTotal = 0
for line in my_numbers:
    numbersTotal += int(line)
print(numbersTotal)
my_numbers.close()