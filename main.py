import tkinter as tk
from PIL import Image, ImageTk

from functions import Data_One, Data_Two, Add_User_Column

root = tk.Tk()
root.title("Report Support Tool")
root.iconbitmap("C:\\Users\\marek\\PycharmProjects\\TeamSupport\\Images\\icon.ico")
canvas = tk.Canvas(root, width=600, height=300, bg="grey")
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open("C:\\Users\\marek\\PycharmProjects\\TeamSupport\\Images\\logo.bmp")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=3, column=0, row=0)

# instrukcje

instructions = tk.Label(root, text="Create your report", font="montserrat", bg="light grey")
instructions.grid(columnspan=1, column=1, row=1)

# Przyciski

button_Data_One = tk.StringVar()
browse_btn = tk.Button(root, textvariable=button_Data_One, command=lambda: Data_One(), font="montserrat",
                       bg="light grey", fg="black", height=1, width=18)
button_Data_One.set("Employees Report")
browse_btn.grid(column=0, row=2, padx=10, pady=10)

button_Data_Two = tk.StringVar()
browse_btn = tk.Button(root, textvariable=button_Data_Two, command=lambda: Data_Two(), font="montserrat",
                       bg="light grey", fg="black", height=1, width=18)
button_Data_Two.set("Department Score")
browse_btn.grid(column=1, row=2, padx=10, pady=10)

button_Add_User_Column = tk.StringVar()
browse_btn = tk.Button(root, textvariable=button_Add_User_Column, command=lambda: Add_User_Column(),
                       font="montserrat", bg="light grey", fg="black", height=1, width=18)
button_Add_User_Column.set("Audit Preparations")
browse_btn.grid(column=2, row=2, padx=10, pady=10)

# canvas = tk.Canvas(root, width=500, height=250)
# canvas.grid(columnspan=3)

root.mainloop()
"""
Kod do instalacji w formacie .exe

pyinstaller --onefile -y -F -w -i "icon.ico" --add-data "*.jpg;." main.py - instalcja z ikoną i grafiką
pyinstaller --onefile -y -F -w -i "icon.ico" main.py - instalcja z ikoną bez grafik

"""
