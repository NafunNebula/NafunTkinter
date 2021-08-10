import math
from tkinter import *

root = Tk()
root.title("Nafun Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

def addEntryValue(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clearEntryValue():
    e.delete(0, END)

def solveEquation():
    result = eval(e.get())
    e.delete(0, END)
    e.insert(0, result)

button1 = Button(root, text="1", padx=50, pady=30, command=lambda: addEntryValue(1))
button2 = Button(root, text="2", padx=50, pady=30, command=lambda: addEntryValue(2))
button3 = Button(root, text="3", padx=50, pady=30, command=lambda: addEntryValue(3))
button4 = Button(root, text="4", padx=50, pady=30, command=lambda: addEntryValue(4))
button5 = Button(root, text="5", padx=50, pady=30, command=lambda: addEntryValue(5))
button6 = Button(root, text="6", padx=50, pady=30, command=lambda: addEntryValue(6))
button7 = Button(root, text="7", padx=50, pady=30, command=lambda: addEntryValue(7))
button8 = Button(root, text="8", padx=50, pady=30, command=lambda: addEntryValue(8))
button9 = Button(root, text="9", padx=50, pady=30, command=lambda: addEntryValue(9))
button0 = Button(root, text="0", padx=50, pady=30, command=lambda: addEntryValue(0))

buttonAdd = Button(root, text="+", padx=50, pady=30, command=lambda: addEntryValue('+'))
buttonSubtract = Button(root, text="-", padx=50, pady=30, command=lambda: addEntryValue('-'))
buttonMultiply = Button(root, text="*", padx=50, pady=30, command=lambda: addEntryValue('*'))
buttonDecimal = Button(root, text=".", padx=50, pady=30, command=lambda: addEntryValue('.'))
buttonEqual = Button(root, text="=", padx=50, pady=30, command=solveEquation)
buttonClear = Button(root, text="C", padx=50, pady=30, command=clearEntryValue)
buttonLeftBracket = Button(root, text="(", padx=50, pady=30, command=lambda: addEntryValue('('))
buttonRightBracket = Button(root, text=")", padx=50, pady=30, command=lambda: addEntryValue(')'))
buttonPi = Button(root, text="π", padx=50, pady=30, command=lambda: addEntryValue(math.pi))
buttonDivide = Button(root, text="÷", padx=50, pady=30, command=lambda: addEntryValue('/'))

buttonClear.grid(row=5, column=0)
button0.grid(row=5, column=1)
buttonDecimal.grid(row=5, column=2)
buttonEqual.grid(row=5, column=3)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
buttonAdd.grid(row=4, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonSubtract.grid(row=3, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
buttonMultiply.grid(row=2, column=3)

buttonLeftBracket.grid(row=1, column=0)
buttonRightBracket.grid(row=1, column=1)
buttonPi.grid(row=1, column=2)
buttonDivide.grid(row=1, column=3)

root.mainloop()

