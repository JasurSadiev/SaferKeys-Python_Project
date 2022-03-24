from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import tkinter.messagebox





objects = []
window = Tk()
window.withdraw()
window.title('SaferKeys')
window.configure(background='#080808', cursor='pirate')



class popupWindow(object):
    

    loop = False
    attempts = 0

    def __init__(self, master):
        top = self.top = Toplevel(master)
        top.configure(bg='#080808', relief='solid', borderwidth=1, highlightcolor= "#02cc20",  highlightthickness=2, highlightbackground="#d91d14")
        top.title('Welcome')
        top.geometry('{}x{}'.format(250, 100))
        top.resizable(width=False, height=False)
        self.l = Label(top, text=" Password: ", relief='raised', font=('Courier', 14), justify=CENTER, foreground= "#02cc20", background='#080808' )
        self.l.pack()
        self.e = Entry(top, show=' ', width=30, foreground="#02cc20", bg='#080808')
        self.e.pack(pady=7)
        self.b = Button(top, text='Submit', command=self.cleanup, font=('Courier', 14), cursor= "plus", bg = '#080808', foreground="#02cc20")
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        access = 'jasur007'

        if self.value == access:
            self.loop = True
            self.top.destroy()
            window.deiconify()
        else:
            self.attempts += 1
            if self.attempts == 5:
                window.quit()
            self.e .delete(0, 'end')
            messagebox.showerror('Incorrect Password', 'Incorrect password, attempts remaining: ' + str(5 - self.attempts))

class entity_add:

    def __init__(self, master, n, p, e):
        self.password = p
        self.name = n
        self.email = e
        self.window = master

    def write(self):
        f = open('emails.txt', "a")
        n = self.name
        e = self.email
        p = self.password

        encryptedN = ""
        encryptedE = ""
        encryptedP = ""
        for letter in n:
            if letter == ' ':
                encryptedN += ' '
            elif letter == '@':
                encryptedN += '@'
            else:
                encryptedN += chr(ord(letter) + 5)

        for letter in e:
            if letter == ' ':
                encryptedE += ' '
            else:
                encryptedE += chr(ord(letter) + 5)

        for letter in p:
            if letter == ' ':
                encryptedP += ' '
            else:
                encryptedP += chr(ord(letter) + 5)

        f.write(encryptedN + ',' + encryptedE + ',' + encryptedP + ', \n')
        f.close()


class entity_display:

    def __init__(self, master, n, e, p, i):
        self.password = p
        self.name = n
        self.email = e
        self.window = master
        self.i = i

        dencryptedN = ""
        dencryptedE = ""
        dencryptedP = ""
        for letter in self.name:
            if letter == ' ':
                dencryptedN += ' '
            else:
                dencryptedN += chr(ord(letter) - 5)

        for letter in self.email:
            if letter == ' ':
                dencryptedE += ' '
            
            else:
                dencryptedE += chr(ord(letter) - 5)

        for letter in self.password:
            if letter == ' ':
                dencryptedP += ' '
            else:
                dencryptedP += chr(ord(letter) - 5)

        self.label_name = Label(self.window, text=dencryptedN, font=('Courier', 13), background = '#080808', foreground='#02cc20')
        self.label_email = Label(self.window, text=dencryptedE, font=('Courier', 13), background = '#080808', foreground='#02cc20')
        self.label_pass = Label(self.window, text=dencryptedP, font=('Courier', 13), background = '#080808', foreground='#02cc20')
        self.deleteButton = Button(self.window, text='X', fg='red', background = '#080808', command=self.delete)

    def display(self):
        self.label_name.grid(row=6 + self.i, sticky=W)
        self.label_email.grid(row=6 + self.i, column=1)
        self.label_pass.grid(row=6 + self.i, column=2, sticky=E)
        self.deleteButton.grid(row=6 + self.i, column=3, sticky=E)

    def delete(self):
        answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')

        if answer == 'yes':
            for i in objects:
                i.destroy()

            f = open('emails.txt', 'r')
            lines = f.readlines()
            f.close()

            f = open('emails.txt', "w")
            count = 0

            for line in lines:
                if count != self.i:
                    f.write(line)
                    count += 1

            f.close()
            readfile()

    def destroy(self):
        self.label_name.destroy()
        self.label_email.destroy()
        self.label_pass.destroy()
        self.deleteButton.destroy()





def onsubmit():
    m = email.get()
    p = password.get()
    n = name.get()
    e = entity_add(window, n, p, m)
    e.write()
    name.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')
    messagebox.showinfo('Added Entity', 'Successfully Added, \n' + 'Name: ' + n + '\nEmail: ' + m + '\nPassword: ' + p)
    readfile()


def clearfile():
    f = open('emails.txt', "w")
    f.close()


def readfile():
    f = open('emails.txt', 'r')
    count = 0

    for line in f:
        entityList = line.split(',')
        e = entity_display(window, entityList[0], entityList[1], entityList[2], count)
        objects.append(e)
        e.display()
        count += 1
    f.close()



m = popupWindow(window)



entity_label = Label(window, text='Write Your Credentials', font=('Times New Roman', 18), background = '#080808', cursor = 'pirate', fg='#02cc20' )
name_label = Label(window, text='Name: ', font=('Times New Roman', 12), foreground='#02cc20', background = '#080808', cursor = '')
email_label = Label(window, text='Email: ', font=('Times New Roman', 12), foreground='#02cc20', background = '#080808', cursor = '')
pass_label = Label(window, text='Password: ', font=('Times New Roman', 12), foreground='#02cc20', background = '#080808', cursor = '')
name = Entry(window, font=('Times New Roman', 12), foreground='#02cc20', cursor = '', background='#080808')
email = Entry(window, font=('Times New Roman', 12), foreground='#02cc20', cursor = '', background='#080808')
password = Entry(window, show=' ', font=('Times New Roman', 12), foreground = '#190BC1', cursor="", background='#080808')
submit = Button(window, text='Add', command=onsubmit, font=('Times New Roman' "bold", 12), foreground='#D81407', background = '#080808', cursor = 'hand2')

entity_label.grid(columnspan=3, row=0)
name_label.grid(row=1, sticky=E, padx=3)
email_label.grid(row=2, sticky=E, padx=3)
pass_label.grid(row=3, sticky=E, padx=3)

name.grid(columnspan=3, row=1, column=1, padx=2, pady=2, sticky=W)
email.grid(columnspan=3, row=2, column=1, padx=2, pady=2, sticky=W)
password.grid(columnspan=3, row=3, column=1, padx=2, pady=2, sticky=W)

submit.grid(columnspan=3, pady=4)

name_label2 = Label(window, text='Name: ', font=('Times New Roman', 12), background='#080808', foreground='#02cc20')
email_label2 = Label(window, text='Email: ', font=('Times New Roman', 12), background='#080808', foreground='#02cc20')
pass_label2 = Label(window, text='Password: ', font=('Times New Roman', 12), background='#080808', foreground='#02cc20')

name_label2.grid(row=5)
email_label2.grid(row=5, column=1)
pass_label2.grid(row=5, column=2)

readfile()

window.mainloop()   
