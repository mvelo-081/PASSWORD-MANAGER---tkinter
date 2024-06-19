import tkinter as tk
from tkinter import messagebox
import random

class my_GUI:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x600')
        self.root.title('Password manager')
        self.label = tk.Label(self.root, text='---PASSWORD MANAGER---', font=('bold', 20))
        self.label.pack(padx=10, pady=10)        
        self.label_create = tk.Label(self.root, text='To Create a file , first name your file by your username', font=('bold', 10))
        self.label_create.pack(padx=10, pady=10)        
        self.text_create_content = tk.StringVar()        
        self.text_create = tk.Entry(self.root, textvariable=self.text_create_content)
        self.text_create.pack(padx=10, pady=10)
        self.button_create = tk.Button(self.root, text='create a file', fg='green', command=self.createAFile)
        self.button_create.pack(padx=10)
        self.just_label = tk.Label(self.root, text='-------------------', font=('bold', 50))
        self.just_label.pack(padx=10, pady=10)        
        self.login_label = tk.Label(self.root, text='To get your passwords , you will need your pin and username you created', font=('bold', 10))
        self.login_label.pack(padx=10, pady=10)        
        self.text_login_username = tk.StringVar()
        self.text_login_pin = tk.StringVar()
        self.just_label = tk.Label(self.root, text='Enter your username below :', font=('bold', 10))
        self.just_label.pack(padx=10, pady=10)
        self.text = tk.Entry(self.root, textvariable=self.text_login_username)
        self.text.pack(padx=10, pady=10)
        self.just_label = tk.Label(self.root, text='Enter your pin below :', font=('bold', 10))
        self.just_label.pack(padx=10, pady=10)
        self.text = tk.Entry(self.root, textvariable=self.text_login_pin)
        self.text.pack(padx=10, pady=10)
        self.confirm_button = tk.Button(self.root, text='Confirm', fg='green', command=self.is_account_exit)
        self.confirm_button.pack(padx=10, pady=10)        
        self.root.mainloop()
    
    def is_account_exit(self):
        username = str(self.text_login_username.get())
        if self.text_login_username is None:
            messagebox.showerror(title='Error', message='Please fill the username!')
        def Account(self):
            username = str(self.text_login_username.get())
            with open('clientAccount.txt', 'r') as readClient:
                for line in readClient:
                        if line.startswith(username):
                            return line.strip()
                        else:
                            continue
        if (username) and (self.text_login_pin.get()):
            if (Account(self) == username):
                print('Account exits')
                GUI_CREATE_PASSWORD(self)
                use_client_username = GUI_CREATE_PASSWORD(app)
                use_client_username.getClientsPasswords()
            elif Account(self) is None:
                messagebox.showerror(title='Error', message=f"The account : '{username}' is not found!")
        else:
            messagebox.showwarning(title='Missing information', message='Fill all the missing details!')
               
        

    def createAFile(self):
        if (self.text_create_content.get()):
            with open(f'{self.text_create_content.get()}.txt', 'w') as cf:
                cf.write('---PASSWORD MANAGER{}---'.format(self.text_create_content.get()))
                messagebox.showinfo(title='info', message=f'You have successfully created a file name of : {self.text_create_content.get()}.txt')
            with open('clientAccount.txt', 'a') as acf:
                acf.write(f"\n\n{self.text_create_content.get()}")
        else:
            messagebox.showwarning(title='Missing information', message='Add a username for your account!')

class GUI_CREATE_PASSWORD:
    def __init__(self, app):
        self.app = app
        self.root = tk.Tk()
        self.root.title('Clients password manager')
        self.root.geometry('500x650')
        self.client_account_label = tk.Label(self.root, text=f'--- {self.app.text_login_username.get()} PROFILE ---', font=('bold', 20))
        self.client_account_label.pack(padx=10, pady=10)
        self.label_gen_pass = tk.Label(self.root, text='Generate password for your account', font=('bold', 10))
        self.label_gen_pass.pack(padx=10, pady=10)   
        self.account_name_create = tk.StringVar()       
        self.entry_gen_password = tk.Entry(self.root, textvariable=self.account_name_create)
        self.entry_gen_password.pack(pady=10)     
        self.button_gen_pass = tk.Button(self.root, text='Generate a password', fg='green', command=self.generateRandomPassword)
        self.button_gen_pass.pack(padx=10)
        self.label_find_pass = tk.Label(self.root, text='To find a saved password under your profile', font=('bold', 10))
        self.label_find_pass.pack(padx=10, pady=10)        
        self.button_show_pass = tk.Button(self.root, text='Show saved passwords', fg='green', command=self.getClientsPasswords)
        self.button_show_pass.pack(padx=10)
        self.label_label_show_passwords = tk.Label(self.root, text='This are saved passwords', font=('bold', 15))
        self.label_label_show_passwords.pack(padx=10, pady=10)
        self.label_show_passwords = tk.Label(self.root, text="click! 'Show saved passwords' button to show saved password", fg='red')
        self.label_show_passwords.pack(padx=10, pady=10)
        self.just_label = tk.Label(self.root, text='------------', font=('bold', 50))
        self.just_label.pack(padx=10, pady=10)
        self.just_label_ = tk.Label(self.root, text='Enter the account name you want to dencrypt it password : ', font=('bold', 10))
        self.just_label_.pack()
        self.decrypt_entry_val = tk.StringVar()
        self.decrypt_entry = tk.Entry(self.root, textvariable=self.decrypt_entry_val)
        self.decrypt_entry.pack(padx=10, pady=10)
        self.button_conf_den = tk.Button(self.root, text='dencrypt', fg='green', command=self.fetchAccountPass)
        self.button_conf_den.pack(padx=10, pady=10)
        self.root.mainloop()

    def getClientsPasswords(self):
        with open(f'{self.app.text_login_username.get()}.txt', 'r') as rf:
            text_content = rf.read()
            self.label_show_passwords.config(text=f"{text_content}")
    def fetchAccountPass(self):
        with open(f'{self.app.text_login_username.get()}.txt', 'r') as ff:
            for line in ff:
                if line.startswith(f'{self.decrypt_entry_val}'):
                    print(line)
                    
    def generateRandomPassword(self):
        def encrypterFun(self):
            encrypterPass = ''
            for char in randomGenPassword:
                encrypterPass += chr(ord(char) % 33 +  33)
            return encrypterPass
        def appendClientPass(self, encryptedPass):
            with open(f'{self.app.text_login_username.get()}.txt', 'a') as apf:
                apf.write(f'{self.app.text_login_username.get()}:{encryptedPass}')
        
        
        randomGenPassword = ""
        for i in range(11):
            randomAsciiValue = random.randint(33, 126)
            randomGenPassword += chr(randomAsciiValue)
        message = f"""
        The Random generated password is {randomGenPassword}
        
        The encrypted password is : {encrypterFun(self, randomGenPassword)} 
        """
        messagebox.showinfo(title='GENERATED PASSWORD', message=message)
        appendClientPass(self, encrypterFun(self, randomGenPassword))


if __name__ == "__main__":
    app = my_GUI()
