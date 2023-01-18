import tkinter as tk
from PIL import Image, ImageTk

from functions import data_one, data_two, add_user_column

root = tk.Tk()
root.title("Report Support Tool")
root.iconbitmap("icon.ico")
canvas = tk.Canvas(root, width=600, height=300, bg="grey")
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open("logo.bmp")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0)


instructions = tk.Label(root, text="Create your report", font="montserrat", bg="light grey")
instructions.grid(columnspan=1, column=1, row=1)


button_Data_One = tk.StringVar()
browse_btn = tk.Button(root, textvariable=button_Data_One, command=lambda: data_one(), font="montserrat",
                       bg="light grey", fg="black", height=1, width=18)
button_Data_One.set("Employees Report")
browse_btn.grid(column=0, row=2, padx=10, pady=10)

button_Data_Two = tk.StringVar()
browse_btn = tk.Button(root, textvariable=button_Data_Two, command=lambda: data_two(), font="montserrat",
                       bg="light grey", fg="black", height=1, width=18)
button_Data_Two.set("Department Score")
browse_btn.grid(column=1, row=2, padx=10, pady=10)

button_Add_User_Column = tk.StringVar()
browse_btn = tk.Button(root, textvariable=button_Add_User_Column, command=lambda: add_user_column(),
                       font="montserrat", bg="light grey", fg="black", height=1, width=18)
button_Add_User_Column.set("Audit Preparations")
browse_btn.grid(column=2, row=2, padx=10, pady=10)


root.mainloop()
