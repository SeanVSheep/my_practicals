import random
help(random.randint)
help(random.randrange)
help(random.uniform)

'''
import random
print(random.randint(5,20))
17

Q: What did you see on line 1?

A: print function calling on a random integer generation function inside the 
random module setting the values to be generated between 5 - 20

Q: What was the smallest number you could have seen, what was the largest?
A:
smallest: 5
largest: 20

print(random.randrange(3, 10, 2))
3

Q: What did you see on line 2?

A; similar to randint, randrange allows us to choose a random number from a range
of numbers with rules to follow, in this case selecting numbers between 3 and 10 
by 2's from three. Only odd numbers will be selected

Q: What was the smallest number you could have seen, what was the largest?

A:
smallest: 3
largest: 9

Q: Could line 2 have produced a 4?

A: no

print(random.uniform(2.5, 5.5))
2.5278393109708213

Q: What did you see on line 3?

A: same as randint line except it can choose from floats with decimal places

Q: What was the smallest number you could have seen, what was the largest?

A: 
smallest: 4.5
largest 5.5
'''
