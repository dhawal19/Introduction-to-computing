#  QUESTION 1
# Taking input of the three numbers
first_number = int(input('enter first number: '))
second_number = int(input('enter second number: '))
third_number = int(input('enter third number: '))
# Applying formula to calculate the average of the three numbers and outputting it
average = (first_number+second_number+third_number)/3

print('The average is: ', average)

# QUESTION 2
# Taking input for the gross income and number of dependents
gross_income = float(input('Enter the Gross income $ '))
no_of_dependents = float(input('Enter number of dependents '))
# Calculating the Taxable income using the formula given
tax_income = gross_income - 10000 - (3000*no_of_dependents)
# Calculating the tax to be paid and outputting it
tax = tax_income * 0.2
if tax < 0:
    print('NO TAX IS TO BE PAID')
else:
 print('Tax is: ', tax, '$')

# QUESTION 3
# Initiating an empty list
Student = []
# Taking input of different data to be stored in the list
sid = Student.append(input('Enter the SID of the student: '))
name = Student.append(input('Enter the name of the student: '))
gender = Student.append(input('Enter the gender of he student (use F, M or U for unknown): '))
course_name = Student.append(input('Enter the course the student id enrolled in: '))
cgpa = Student.append(float(input('Enter the CGPA of the student: ')))
# Outputting  the collected data of the student
print('The details of the student are: ', Student)

#QUESTION 4
# Initiating an empty list
Marks = []

# Taking input of the marks of the 5  students
marks_1 = Marks.append(int(input('Enter the marks of student 1: ')))
marks_2 = Marks.append(int(input('Enter the marks of student 2: ')))
marks_3 = Marks.append(int(input('Enter the marks of student 3: ')))
marks_4 = Marks.append(int(input('Enter the marks of student 4: ')))
marks_5 = Marks.append(int(input('Enter the marks of student 5: ')))

# Outputting the marks of the 5 students in sorted list
Marks.sort()
print('The marks of the students are: ', Marks)

#QUESTION 5(a)
# Defining the list color
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Removing the fourth element from the given list and outputting the new list
color.remove(color[3])
print('The new list is ', color)

#QUESTION 5(b)
# Defining the list colors
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Replacing Black and Pink with Purple
color[3] = 'Purple'
color.remove(color[4])
print('The edited list is ', color)
