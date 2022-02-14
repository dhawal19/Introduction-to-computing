# Question 1
# Defining a function to calculate occurrences of string elements
def occurrence_calculator(lst):
    empty = []
# Using dictionaries to display number of occurrences of the elements
    occurrence = {lst[i]: 1 for i in range(0, len(lst))}
# Loop to update values of different elements
    for char in lst:
        if char in empty:
            occurrence[char] += 1
        else:
            empty.append(char)
    print(occurrence, '\n')


# Taking input string from the user
string = input("Enter the string: ")
# Checking if the entered string is a single word or a sentence
if " " not in string:
    letters = list(string)
    occurrence_calculator(letters)

else:
    words = string.split()
    occurrence_calculator(words)


# Question 2
# Defining functions to change date and month
def month_change(d, m):
    d = 1
    m += 1
    return d, m


def day_change(date):
    date += 1
    return date


# Taking input of the date from user
day = int(input('Enter the date: '))
month = int(input('Enter the month: '))
year = int(input('Enter the year: '))
months_31 = [1, 3, 5, 7, 8, 10, 12]
months_30 = [4, 6, 9, 11]
# Applying conditions for different cases using if/elif/else
if 1 <= month <= 12 and 1 <= day <= 31 and 1800 <= year <= 2025:
    if month in months_31:
        if day == 31:
            #   Checking for New Year's Eve
            if month == 12:
                day = 1
                month = 1
                year += 1
            else:
                day, month = month_change(day, month)

        else:
            day = day_change(day)
    elif month in months_30:
        if day == 30:
            day, month = month_change(day, month)
        elif day == 31:
            print('Invalid date')
            exit()
        else:
            day = day_change(day)
    elif month == 2:
        # Checking for leap year
        if year % 4 == 0:
            if day == 29:
                day, month = month_change(day, month)
            elif day == 30 or day == 31:
                print('Invalid date')
                exit()
            else:
                day = day_change(day)
        else:
            if day == 28:
                day, month = month_change(day, month)
            elif day == 29 or day == 30 or day == 31:
                print('Invalid date')
                exit()
            else:
                day = day_change(day)
#  If the entered date is not in the set range, then outputting invalid
else:
    print('Invalid date has been entered!\n')
    exit()
print(f'Next date: {day}/{month}/{year}\n')


# Question 3
# Taking input of a  list of numbers from the user
length = int(input('Enter number of elements: '))
lst = []
squares = []
for num in range(0, length):
    lst.append(int(input(f'Enter list element {num+1}: ')))
# Appending the squares of the list elements to another list
for nums in lst:
    squares.append(nums**2)
# Using zip creating a list of tuples with user defined list the squares of its elements
squared_list = list(zip(lst, squares))
print(squared_list, '\n')


# Question 4
# Taking the grade point from the user in range 4  to 10
grade = int(input('Enter grade point between 4 and 10: '))
if grade in range(4, 11):
    # Using dictionaries to map grade point to letter grade and performance remark
    letter_grade = {4: 'D', 5: 'C', 6: 'C+', 7: 'B', 8: 'B+', 9: 'A', 10: 'A+'}
    performance = {4: 'Poor', 5: 'Below Average', 6: 'Average', 7: 'Good', 8: 'Very Good', 9: 'Excellent',
                   10: 'Outstanding'}
    print(f"Your Grade is '{letter_grade[grade]}' and {performance[grade]}\n")
# Printing error message if the grade point is out of range
else:
    print('Error! Grade should be between 4 and 10\n')


# Question 5
# Program to print alphabet pattern using string library
import string

rows = int(input('Enter the number of rows in the pattern: '))
# Using string library function to create a string of uppercase alphabets
alpha = string.ascii_uppercase
# Rows can be between 1 and 13
if 1 <= rows <= 13:
    # Using nested for loop to create the pattern
    for i in range(rows, 0, -1):
        for j in range(0, rows-i):
            print(end=' ')
        print(alpha[0:(2 * i - 1)])
# Printing error message if invalid no. of rows is entered
else:
    print('Enter no. of rows between 1 and 13.')


# Question 6
# Initialising an empty dictionary
details = {}
ans = 'Y'
# Looping to get Name and SID of the students and adding them as key-value pairs to the dictionary
while ans.upper() == 'Y':
    name = input("Enter name of the student: ")
    sid = int(input('Enter SID of the student:  '))
    details.update({sid: name})
    ans = input('Do you want to add student details? ')
# Part (a)
print(details, '\n')
# Part (b)
print(sorted(details.items(), key=lambda x: x[1]), '\n')
# Part(c)
for i in sorted(details):
    print((i, details[i]), end=' ')
print('\n')
# Part (d)
# Taking name of the student whom details are to be searched
search_sid = int(input('Enter SID of the student to be searched: '))
if search_sid in details:
    print('Name of the student: ', details[search_sid], '\n')
else:
    print('Student details with this SID is not present in thr hash.')

# Question 7
# Taking input for the terms required.
Total_Terms=int(input("Enter the number of fibonacci terms you want:- \n"))
First_Term=0
Next_Term=1
Nth_Term=0
Sum=0
# Using for loop to get the n terms

for i in range(1,Total_Terms+1):
    
    if(i==1):
        print(0)
    elif (i==2):
        print(1)
        Sum=Sum+1
    else:
        Nth_Term=First_Term+Next_Term
        Sum=Sum+Nth_Term
        print(Nth_Term)
        First_Term=Next_Term
        Next_Term=Nth_Term
print("The Average of the numbers is:-", float(Sum/Total_Terms))
print('\n')


# Question 8
# Initialising Sets 
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# Part (a)
Part_a = Set1 ^ Set2
print('Part a: ', Part_a)
# Part (b)
Part_b = Set1 ^ Set2 ^ Set3
print('Part b: ', Part_b)
# Part (c)
Part_c = Set1 & Set2 | Set2 & Set3 | Set1 & Set3
print('Part c: ', Part_c)
# Part (d)
Part_d = set(range(1, 11)) - Set1
print('Part d: ', Part_d)
# Part (e)
Part_e = Part_d - Set2 - Set3
print('Part e: ', Part_e, '\n')
