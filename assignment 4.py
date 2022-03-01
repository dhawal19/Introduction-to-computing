# Question 1
# Defining a recursive function to print the moves to solve tower of hanoi problem
def tower_hanoi(n, start, end):
    if n == 1:
        print_moves(n, start, end)
    else:
        other = 6 - (start + end)
        tower_hanoi(n-1, start, other)
        print_moves(n, start, end)
        tower_hanoi(n-1, other, end)


# Function to print the moves denoting the initial position of a disk and the destination position
def print_moves(n, start, end):
    print(f'Moved disc {n} from rod {start} to rod {end}')


# Calling the function to solve for three disks. Here 1 denotes the starting position and 3 denotes the last position.
tower_hanoi(3, 1, 3)
print('\n\n')

# Question 2
# Defining recursive function to calculate factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        fact = num * factorial(num-1)
        return fact


# Defining a function to generate pascal's triangle using iteration
def pascals_triangle_iter(rows):
    for i in range(rows):
        for j in range(rows - i + 1):
            # for left spacing
            print(end=" ")

        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

        # for new line
        print()


# Defining a recursive function to generate pascal's triangle pattern
def pascals_triangle_recursive(num):
    if num == 1:
        return [[1]]  # Base case condition
    else:
        result = pascals_triangle_recursive(num - 1)
        # Calculate current row using info from previous row
        current_row = [1]
        # Creating list by taking from end of result
        previous_row = result[-1]
        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])
        current_row += [1]
        result.append(current_row)
        return result


rows = int(input('Enter no of rows: '))
pascals_triangle_iter(rows)
pascal_triangle = pascals_triangle_recursive(5)
print('\n')
for row in pascal_triangle:
    print(row)
print('\n\n')


# Question 3
dividend = int(input("Enter the dividend: "))
# To check that the denominator is not zero, loop is defined.
while True:
    divisor = int(input("Enter the divisor: "))
    if divisor != 0 and divisor > 0:
        break
    else:
        print("\nThe divisor must be greater than 0.\nPlease enter the divisor again.")
quotient = dividend // divisor
remainder = dividend % divisor

print("Quotient = ", quotient)
print("Remainder = ", remainder)

# part (a)
print("(a) \n")
print("Checking whether the quotient and remainder are callable values or not.")
print(callable(quotient))
print(callable(remainder), '\n\n')

# part (b)
print("(b) \n")
if quotient == 0 & remainder == 0:
    print("Both quotient and remainder are zero. \n")
if quotient == 0 & remainder !=0:
    print("Quotient is zero while remainder is non zero. \n")
if quotient != 0 and remainder == 0:
    print("Quotient is non zero while remainder is zero. \n")
if quotient != 0 and remainder != 0:
    print("Both quotient and remainder are non zero. \n\n")

# part (c)
print("(c) \n")
result = [quotient + 4, remainder + 4, quotient + 5, remainder + 5, quotient + 6, remainder + 6]

filter_result = []
for i in range(len(result)):
    if result[i] > 4:
        filter_result.append(result[i])
print(f'The filtered numbers that are greater than 4 are : {filter_result} \n\n')

# part (d)
print("(d) \n")
set_result = set(filter_result)
print('Set:', set_result, '\n\n')

# part (e)
print("(e) \n")
immutable_set = frozenset(set_result)
# Frozen Set function is used to make the set immutable.
print('Immutable set: ', immutable_set, '\n\n')

# part (f)
print("(f) \n")
print("Hash value of the max value from the above set:- ", hash(max(immutable_set)), '\n\n')


# Question 4
# Defining a class and its constructor and destructor
class Student:
    def __init__(self, student, roll_no):
        self.name = student
        self.rollno = roll_no

    def __del__(self):
        print('Object has been deleted.')


# Creating object
student1 = Student('Dhawal', 21103034)
print("Object has been created. ")
# Printing the default values.
print(f'The name of the student is {student1.name} and SID is {student1.rollno}.')
# Deleting the object by calling destructor.
del student1
print('\n\n')

# Question 5
# Defining a class to store employee data.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_data(self):
        print("%s has a salary of %d rupees" % (self.name,self.salary))


# Initialising employee data with given values
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)
# Printing the initial values
print('The current database is: ')
for emp in [employee1, employee2, employee3]:
    emp.print_data()

# Part (a)
employee1.salary = 70000
print('(a)\n')
print(f'The updated salary of {employee1.name} is {employee1.salary} rupees \n')
# Part (b)
print('(b)\n')
del employee3
print('Record of Viren deleted', end='')
print('\n\n')


# Question 6
# Defining anagram function
def anagram(string):
    if len(string) == 1:
        return [string]
    other_words = anagram(string[1:])
    first_letter = string[0]
    anagrams = []
    for combination in other_words:
        for i in range(len(combination)+1):
            anagrams.append(combination[:i] + first_letter + combination[i:])
    return anagrams


# Inputting George's and Barbie's words.
george_word = input("George's word:-").lower()
barbie_word = input("Barbie's word:-").lower()
# Calling the anagram function
other_words = anagram(george_word)
print("Now we shall judge the credibility of their friendship! \n")
# Using if else to check the condition
if barbie_word in other_words:
    print("The Friendship is real.")
else:
    print("The Friendship is fake.")
