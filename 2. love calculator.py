# Python Tkinter GUI based "which thing you like percentage CALCULATOR"

# import tkinter
from tkinter import *
# import random module
import random
# Creating GUI window
root = Tk()
# Defining the container size, width=100, height=100
# root.geometry('100x100')
# Title of the container
root.title('Love Calculator limited edition')

# Function to calculate which thing you like most
# and the percentage of love between the user ans and the thing or person you like


def calculate_love():
	# value will contain digits between 0-100
	st = '0123456789'
	# result will be in double digits
	digit = 2
	temp = "".join(random.sample(st, digit))
	result.config(text=temp)


# Heading on Top
heading = Label(root, text='Love Calculator - How much is he/she like you')
heading.pack()

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="enter 2 person name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="Calculate", height=1,
			width=7, command=calculate_love)
bt.pack()

# Text on result slot
result = Label(root, text='Percentage of love between both of You:')
result.pack()

# Starting the GUI
root.mainloop()
