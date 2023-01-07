from tkinter import *
from tkinter import messagebox
from functools import partial

isim = "Alone"
şifre = "burak"

def open_win():
   kapat()
   tkWindow = Toplevel()
   tkWindow.geometry("750x250")
   tkWindow.title("AloneProjects Panel")
   tkWindow.configure(background='#7cc28a')
   usernameLabel = Label(tkWindow, text="AloneProjects Kullanıcı Paneli", bg='#7cc28a', fg='#2e6e3b', font=('Montserrat', 20, 'bold')).grid(row=2, column=6, padx=(175, 0))

   
def yanlis():
    messagebox.showerror("Giriş Sistemi", "Şifre veya kullanıcı adı hatalı")
    
def dogru():
    messagebox.showinfo("Giriş Sistemi", "Başarılı")
    
def kapat():
    tkWindow.destroy()
    
def validateLogin(username, password):
    if username.get() == isim:
     if password.get() == şifre:
       print("doğru")
       dogru()
       open_win()
    else:
        print("yanlış")
        yanlis()
    return
	#print("Kullanıcı :", username.get())
	#print("şifre :", password.get())
	#return

#window
tkWindow = Tk()  
tkWindow.geometry('300x200')  
tkWindow.title('AloneProjects Giriş')
tkWindow.configure(background='#7cc28a')
tkWindow.resizable(False, False)


#username label and text entry box
usernameLabel = Label(tkWindow, text="Kullanıcı", bg='#7cc28a', fg='#2e6e3b').grid(row=2, column=3, padx=(90, 0))
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=3, column=3, padx=(90, 0))  

    
#password label and password entry box
passwordLabel = Label(tkWindow,text="Şifre", bg='#7cc28a', fg='#2e6e3b').grid(row=4, column=3, padx=(90, 0))  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=5, column=3, padx=(90, 0))  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Giriş", command=validateLogin, bg='#7cc28a', fg='#2e6e3b', height=2, width=16).grid(row=7, column=3, padx=(90, 0))  

tkWindow.mainloop()