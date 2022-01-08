#Answer 1
print("Answer 1.")

#input numbers
num1 = int(input("Enter number 1. - "))
num2 = int(input("Enter number 2. - "))
num3 = int(input("Enter number 3. - "))

sum = num1 + num2 + num3
average = sum / 3

print(average)
#____________________________________________________

#Answer 2
print("\n\nAnswer 2.")

#input income and dependents
grossincome = float(input("Enter Gross Income - "))
dependents = int(input("Enter Dependents - "))

#tax calculation
taxincome = grossincome - 10000 - (dependents * 3000)
tax = taxincome * 0.20

print("tax:",round(tax,2))
#____________________________________________________

#Answer 3
print("\n\nAnswer 3.")

l = []
#Input details
l.append(input('Enter SID:'))
l.append(input('Enter Name:'))
l.append(input('Enter Gender(F, M, or U):'))
l.append(input('Enter Course Name:'))
l.append(float(input('Enter CGPA:')))
print(l)
#____________________________________________________

#Answer 4
print("\n\nAnswer 4.")

#input marks in one go
marks = list(map(int, input("Enter the marks of all the 5 students:").split()))
marks.sort()
print(marks)
#____________________________________________________

#Answer 5
print("\n\nAnswer 5.")

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# answer for a, removing element
color.remove('Black')
print("color",color)

# answer for b, replacing black and pink with purple
# redefine color
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5] = ['Purple']
print("color",color)
