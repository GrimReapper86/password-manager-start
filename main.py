from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_input.delete(0, END)
    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char1 in range(randint(2, 4))]
    password_list += [choice(numbers) for char2 in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input.get(), message=f"These are details entered : \n"
                                                                          f"Email{user_input.get()}"
                                                                          f"\nPassword:{password_input.get()}\n"
                                                                          f"Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_input.get()}|{user_input.get()}|{password_input.get()}\n")
            website_input.delete(0, END)
            user_input.delete(0, END)
            user_input.insert(0, "-@gmail.com")
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, )
# labels

website_label = Label(text="WebSite", padx=20, pady=5)
website_label.grid(row=1, column=0, sticky="E")
user_label = Label(text="Email/ Username", padx=20, pady=5)
user_label.grid(row=2, column=0, sticky="E")
password_label = Label(text="Password", padx=20, pady=5)
password_label.grid(row=3, column=0, sticky="E")
# input interface
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="W")
user_input = Entry(width=35)
user_input.insert(0, "-@gmail.com")
user_input.grid(row=2, column=1, columnspan=2, sticky="W")
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="W")
# buttons
gen_pass_button = Button(text="Generate password", highlightthickness=0, command=pass_generator)
gen_pass_button.grid(row=3, column=2, sticky="W")
add_button = Button(text="Add", highlightthickness=0, width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")
window.mainloop()
