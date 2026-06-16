def student(name, age, studentnumber, course):
   
    print('My name is ', name )
    print ('My age is ', age)
    print('I do ', course)
    print('My student number is ', studentnumber)

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
course = input('Please enter your course: ')
studentnumber = input('Please enter student number: ')
student(name, age,studentnumber,course)
