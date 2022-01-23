# Question 1
# Initialising the string
string = 'Python is a case sensitive language'
# Part a) Printing the length of the given string
print('The length of the given string is ', len(string))
# Part b) Reversing the given string
print('The reversed string is ', string[::-1])
# Part c) Slicing the string and storing it as another string
slice_str = string[11:27]
print('The sliced string is ', slice_str)
# Part d) Replacing 'a case sensitive' with 'object orientated' in the given string
print('The string after replacing is ', string.replace('a case sensitive', 'object orientated'))
# Part e) Finding the index of 'a' in the given string
print("The index of 'a' in the given string is ", string.index('a'))
# Part f) Removing the spaces from the given string
print('The string after removing spaces is ', string.replace(' ', ''), '\n\n')

# Question 2
# Taking input of details of the student
name = input('Enter your name: ')
sid = input('Enter your SID: ')
cgpa = input('Enter your CGPA: ')
dept_name = input('Enter your Department name: ')
# Printing the details n the given format using fstring
print(f'Hey, {name} here! \n'
       f'My SID is {sid}\n'
       f'I am from {dept_name} and my CGPA is {cgpa}\n \n')

# Question 3
# Initiating a and b with values 56 and 10 respectively.
a = 56
b = 10
# Implementing bit-wise operator and (&)
print('Calculated a&b = ', a & b)
# Implementing bit-wise operator or (|)
print('Calculated a|b = ', a | b)
# Implementing bit-wise operator xor (^)
print('Calculated a^b = ', a ^ b)
# Implementing left shift bit-wise operator
print(f'After left shifting both a and b by 2 bits, a = {a<<2} and b = {b<<2}.')
# Implementing right shift bit-wise operator
print(f'After right shifting a with 2 bits and b with 4 bits, a = {a>>2} and b = {b>>4} \n \n')

# Question 4
# Taking input of the three numbers as integers
first_num = int(input('Enter the first number '))
second_num = int(input('Enter the second number '))
third_num = int(input('Enter the third number '))
# Applying the logic using if else statements and printing the greatest number of the three.
# It first compares the first number with the second and then with the third returning whichever is the greatest.
if first_num > second_num:
       if first_num > third_num:
          print('The greatest  number is: ',  first_num,'\n\n')
       else: print('The greatest  number is: ', third_num, '\n\n')
# If the second number is greater than the first than it compares it with third number and returns the greatest number.
elif second_num > third_num:
         print('The greatest  number is: ', second_num, '\n\n')
else: print('The greatest  number is ', third_num, '\n\n')

# Question 5
# Taking input string from the user
string = input('Enter the string to be checked ')
# Implementing if else statements to check if the string contains the word 'name'.
if 'name' in string:
    print('Yes \n\n')
else: print('No \n\n')

# Question 6
# Inputting the length of a sides and storing them into a list.
sides = [int(input('Enter the length of first side ')), int(input('Enter the length of second side ')),
         int(input('Enter the length of third side '))]
# Implementing if else statement to check if any of the three lengths is greater than the sum of the other two.
# If that is the case then a triangle can't be formed, otherwise it can be.

if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1]:
    print('No \n\n')
else:
    print('Yes \n\n')














