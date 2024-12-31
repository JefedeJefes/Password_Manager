import tkinter
from gc import collect
from tkinter import messagebox
from random import choice , randint , shuffle , random
import pyperclip




'''password generator'''
#Password Generator Project
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(0,10))]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    # for char in range(nr_numbers):
    #    password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password="".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)




'''''Data_handling save password in file '''''
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) ==0 or len(password) ==0:
        messagebox.showinfo(title="Opps!",message="Please make sure you haven't left anything empty")

    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered \n website : {website}\n email : {email}\n password : {password}\n Is it ok to Save? ")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,tkinter.END)
                password_entry.delete(0,tkinter.END)







'''main'''


window = tkinter.Tk()
window.title("Password Manager")
window.minsize(height=230,width=230)
window.config(padx=20,pady=20)

canvas = tkinter.Canvas(width=200,height=200)
photo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text =      "Website:")
website_label.grid(row=1,column=0)
email_label = tkinter.Label(text = "Email/Username:")
email_label.grid(row=2,column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3,column=0)



website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"arjun.vyas@vyas.com")


password_entry = tkinter.Entry(width=35)
password_entry.grid(row=3,column=1,columnspan=2)


generate_button= tkinter.Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

add_button = tkinter.Button(text="Add",width=30,command=save)
add_button.grid(row=4,column=1,columnspan = 2)





tkinter.mainloop()