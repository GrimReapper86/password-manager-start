from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_input.delete(0, END)
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# -------------------------- Find Password ---------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title=f'File Not Found', message="Create a file by adding "
                                                             "an email address or refer to the file path")
    else:
        if website_input.get() in data:
            messagebox.showinfo(title=f" {website_input.get()} ",
                                message=f"Email :  {data[website_input.get()]['email']} \n"
                                        f"Password :{data[website_input.get()]['password']}")
        else:
            messagebox.showinfo(title="Not Found", message="Website not found in the database!")


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
website_input = Entry(width=21)
website_input.focus()
website_input.grid(row=1, column=1, sticky="W")
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
search_button = Button(text="Search", highlightthickness=0, command=find_password)
search_button.grid(row=1, column=2, sticky="W")
window.mainloop()
