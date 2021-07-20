# File:     binary-converter.py
# Author:   r0paire
# Repo:     https://www.github.com/r0paire/binary-converter-app
# Date:     20/07/2021
# Info:     App that converts text to binary or converts binary to text
# Python:   Python-3.9

# Imports
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont

# Setup
app = Tk()
app.title("Binary converter")
app.configure(bg="black")
app.iconphoto(False, tkinter.PhotoImage(file="binary-icon.png"))
app.geometry("800x800")
app.resizable(False, False)

# Fonts
headerFont = tkFont.Font(family="Terminal", size=12)
labelFont = tkFont.Font(family="Terminal", size=11)


# Function to clear text & binary fields
def clear():
    textBox.delete(1.0, "end")
    binaryBox.delete(1.0, "end")


# Text-to-Binary function for Convert()
def text2binary(text, encoding='utf-8', errors='surrogatepass'):
    try:
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        binary = bits.zfill(8 * ((len(bits) + 7) // 8))
        binaryBox.insert(1.0, binary, "end")
        return binary
    except (UnicodeDecodeError, ValueError) as e:
        messagebox.showinfo("Error: invalid string", "Please enter a valid text string")
        clear()


# Binary-to-Text function for Convert()
def binary2text(bits, encoding='utf-8', errors='surrogatepass'):
    try:
        n = int(bits, 2)
        text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
        textBox.insert(1.0, text, "end")
        return text
    except (UnicodeDecodeError, ValueError) as e:
        messagebox.showinfo("Error: invalid binary", "Please enter a valid binary string")
        clear()


# Conversion function
def convert():
    if r.get() == 1:
        binaryBox.delete(1.0, "end")
        text = textBox.get("1.0", 'end-1c')
        text2binary(text, encoding='utf-8', errors='surrogatepass')

    elif r.get() == 2:
        textBox.delete(1.0, "end")
        bits = binaryBox.get("1.0", 'end-1c')
        binary2text(bits, encoding='utf-8', errors='surrogatepass')

    else:
        print("error in else")


# Labels & TextBoxes
# Header
header = Label(app, text="Binary Converter", font=headerFont, fg="lime", bg="#121212", height="4", width="114")
header.pack()

# Text
textLabel = Label(app, text="Text:", font=labelFont, fg="lime", bg="black")
textLabel.place(x=50, y=120)
textBox = Text(app, fg="lime", bg="#202020", height=10, width=87)
textBox.place(x=50, y=140)

# Binary
binaryLabel = Label(app, fg="cyan", bg="black", text="Binary:", font=labelFont)
binaryLabel.place(x=50, y=410)
binaryBox = Text(app, fg="lime", bg="#202020", height=10, width=87)
binaryBox.place(x=50, y=430)

# Author
author = Label(app, text="r0paire© 2021", font=('Ubuntu', 8, 'bold italic'), fg="red", bg="#121212")
author.place(x=715, y=50)

# Radio Buttons
r = IntVar(0)

textBtn = Radiobutton(app, text="Text", fg="lime", bg="black", variable=r, value=1)
textBtn.place(x=295, y=635)
binaryBtn = Radiobutton(app, text="Binary", fg="cyan", bg="black", variable=r, value=2)
binaryBtn.place(x=450, y=635)

# Buttons
convBtn = Button(app, text="Convert", command=convert, height="4", width="30", fg="black", bg="lime")
convBtn.place(x=290, y=700)
clearBtn = Button(app, text="Clear", command=clear, height="4", width="30", fg="white", bg="blue")
clearBtn.place(x=50, y=700)
quitBtn = Button(app, text="Exit", command=app.destroy, height="4", width="30", fg="white", bg="red")
quitBtn.place(x=530, y=700)

app.mainloop()
