from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#####################################

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# The image used https://drive.google.com/file/d/12EFnmf-piegeBTb86-BfCXAStqogTvqd/view?usp=sharing
######################################
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random.shuffle(letters)
    random.shuffle(numbers)
    random.shuffle(symbols)

    user_letters = random.randint(8, 10)
    user_numbers = random.randint(2, 4)
    user_symbols = random.randint(2, 4)

    password_letters = ""
    for letter in range(user_letters):
        password_letters += letters[letter]

    password_numbers = ""
    for number in range(user_numbers):
        password_numbers += numbers[number]

    password_symbol = ""
    for symbol in range(user_symbols):
        password_symbol += symbols[symbol]
    password = password_letters + password_numbers + password_symbol

    strings_to_list = list(password)
    random.shuffle(strings_to_list)

    final_password = "".join(strings_to_list)

    password_entry.insert(0, final_password)
    
    pyperclip.copy(final_password)

##############################

def save():
    website = website_entry.get()
    email = email_entry.get()
    passwd = password_entry.get()

    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation", message=f"These are the details entered: \nEmail: {email} "
                                                                     f"\nPassword: {passwd} \nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {passwd}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


########################################
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Entries
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # sets cursor-input position
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "lexis@gmail.com")  # sets default text in email field
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
