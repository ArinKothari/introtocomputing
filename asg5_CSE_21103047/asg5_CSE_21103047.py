#Answer 1
print("Answer 1.")

from tkinter import *

#creating gui object
win = Tk()
win.title("GST Tax Finder")

#variables for storing original cost and net price
cost_var = StringVar()
price_var = StringVar()

#creating labels
cost_label = Label(win, text="Original Cost")
price_label = Label(win, text="Net Price")

#creating entry boxes
cost_entry = Entry(win, textvariable = cost_var)
price_entry = Entry(win, textvariable = price_var)

#function for calculating tax
def submit():
    cost = cost_var.get()
    price = price_var.get()
    answer = ((int(price) - int(cost)) * 100 ) / int(cost)
    label.config(text = f"The GST Rate is {answer}")

#creating submit button
button = Button(win, text = "Calculate", command= submit)

#placing all the objects
cost_entry.grid(row = 0, column =1)
cost_label.grid(row = 0, column =0)
price_entry.grid(row = 1, column =1)
price_label.grid(row = 1, column =0)
button.grid(row = 2, column = 1)

#printing answer
label = Label(win)
label.grid(row=3,column=1)

win.mainloop()

#____________________________________________________

#Answer 2
print("\n\nAnswer 2.")

from calendar import calendar
from tkinter import *

#creating gui object
win = Tk()
win.title("Calendar")
win.geometry("500x600")

#variable for year
year_var = StringVar()

#creating lables
label = Label(win, text = "Enter year")
calender = Label(win)

#creating entry
entry = Entry(win, textvariable = year_var)

#function to display calendar
def submit():
    year = year_var.get()
    calender.config(text=calendar(int(year)))
    print(calendar(int(year)))
    

#creating submit button
button = Button(win, text = "Display", command= submit)

#placing the objects
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calender.grid(row=2, column=0)
button.grid(row=1, column=1)
calender.grid(row=2, column=1)

win.mainloop()

#____________________________________________________

#Answer 3
print("\n\nAnswer 3.")

from tkinter import *

#creating gui object
win = Tk()
win.title("Calculator")
win.geometry("200x200")

#variables
num1 = StringVar()
num2 = StringVar()

#entries
entry1 = Entry(win, textvariable=num1, width=8)
entry2 = Entry(win, textvariable=num2, width=8)

#calculations
#printing on both gui and terminal
def addition():
    label.config(text = int(num1.get()) + int(num2.get()))
    print(int(num1.get()) + int(num2.get()))

def subtraction():
    label.config(text = int(num1.get()) - int(num2.get()))
    print(int(num1.get()) - int(num2.get()))

def multiplication():
    label.config(text = int(num1.get()) * int(num2.get()))
    print(int(num1.get()) * int(num2.get()))

def division():
    label.config(text = int(num1.get()) / int(num2.get()))
    print(int(num1.get()) / int(num2.get()))

#buttons
add = Button(win, text="+", command=addition)
sub = Button(win, text="-", command=subtraction)
mul = Button(win, text="x", command=multiplication)
div = Button(win, text="/", command=division)

#label
label = Label(win)
label1 = Label(win, text = "Number 1")
label2 = Label(win, text = "Number 2")

#placing all the objects
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
add.grid(row=2, column=0)
sub.grid(row=2, column=1)
mul.grid(row=3, column=0)
div.grid(row=3, column=1)
label.grid(row=4, column=1, pady=10)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

win.mainloop()

#____________________________________________________

#Answer 4
print("\n\nAnswer 4.")

def sort(start, end, array):
	
	#defining the pivot which in this case will be the first element
	pivot_index = start
	pivot = array[pivot_index]
	
	while start < end:
		
        #keeping track of index of smaller element
		while start < len(array) and array[start] <= pivot:
			start += 1
			
        #keeping track of the index where larger elements start
		while array[end] > pivot:
			end -= 1
		
		#swapping the larger value in start index with smaller value in end index
		if(start < end):
			array[start], array[end] = array[end], array[start]
	
	array[end], array[pivot_index] = array[pivot_index], array[end]
	
	#returning the pivot index which splits the array 
	return end
	
def quick_sort(start, end, array):
	
	if (start < end):
		p = sort(start, end, array)
        #and finally the recursive sorting
		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)
		
# inputing the array and quick sorting it
array = list(map(int, input("Enter the array: ").split()))
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')

#____________________________________________________

#Answer 5
print("\n\nAnswer 5.")

array = list(map(int, input("Enter an integer array  containing duplicates: ").split()))
#part a
#using the above quicksort function to sort the array
quick_sort(0, len(array)-1, array)
print("a. Sorted array: ", array)

#part b
def binary(x, arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            #ignore second half
            high = mid - 1
        elif arr[mid] < x:
            #ignore first half
            low = mid + 1
        else:
            #x is equal to value at mid
            return mid
    
    #the list got empty so we got out of while
    #meaning the element is not present
    return -1

x = int(input("Enter the number to find: "))
result = binary(x, array)
if result == -1:
    print("b. Element is not present in array")
else:
    print("b. Element is present at index",str(result))

#part c
count = 0
for i in range(len(array)):
    if array[i] == x:
        count += 1
print(f"c. The number of occurrences of {x} is {count}")
