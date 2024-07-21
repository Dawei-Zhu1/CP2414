"""
This python program is a collection of previous tasks to build a password manage system.
By Zhu Dawei
"""
import os.path
import shutil

import input_checking
import password_management
from password_management import *

import facial_recognition
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

PADDING = 10
LABEL_WIDTH = 10

core = PasswordManagement()


class Main:
    def __init__(self):
        self.root = tk.Tk()
        HomeView(self.root)
        self.root.mainloop()


class View:
    def __init__(self, master: tk.Tk, title='', geometry='400x200'):
        master.title(title)
        master.geometry(geometry)


class HomeView(View):
    def __init__(self, master: tk.ttk) -> None:
        super().__init__(master)
        self.master = master
        self.master.title('Password Management UI - Home Page')

        tk.Frame(master).pack(anchor=tk.CENTER, padx=PADDING, pady=15)
        tk.Button(text='Login', width=10, command=new_login_window).pack()
        tk.Button(text='Register', width=10, command=new_register_window).pack()
        tk.Button(text='Show Accounts', width=10, command=new_show_accounts).pack()


class Row(tk.Frame):
    """
    Generate row like:
    [Label] [Input box]
    """

    def __init__(self, master: tk.Frame, label, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.label = tk.Label(self, text=label, width=LABEL_WIDTH, anchor=tk.W)
        self.entry = tk.Entry(self)
        self.label.pack(side=tk.LEFT)
        self.entry.pack(side=tk.LEFT)
        self.pack()

    def clear(self):
        """
        Clear the text box
        """
        self.entry.delete(0, tk.END)

    def set(self, text) -> None:
        """
        Set text value
        """
        self.entry.insert(0, text)

    def get(self):
        """
        Return the text
        """
        return self.entry.get()


class PasswordRow(Row):
    def __init__(self, master: tk.Frame, label, **kwargs):
        super().__init__(master, label, **kwargs)
        self.entry.config(show='*')


class RowForPhoto(Row):
    def __init__(self, master: tk.Frame, label, **kwargs):
        super().__init__(master, label, **kwargs)
        self.select_photo_btn = tk.Button(self, text='...', command=self.select_photo)
        self.select_photo_btn.pack(side=tk.LEFT)

    def select_photo(self):
        photo_direction = facial_recognition.input_photo()
        if photo_direction:
            # If there is any thing in the box, it will not be emptied.
            self.entry.delete(0, tk.END)
        self.entry.insert(0, photo_direction)


class Form(tk.Frame):
    def __init__(self, master: tk.Frame, **kwargs):
        super().__init__(master, height=100, width=200, **kwargs)
        self._master = master

        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.TOP)

        self.name = Row(self.frame, 'Name')
        self.password = Row(self.frame, 'Password')
        self.photo_directory = RowForPhoto(self.frame, 'Your photo')

        self.pack(padx=PADDING, pady=PADDING)

        # Select all when password is selected
        self.password.bind("<FocusIn>", self.select_all)

        # Generate a password
        self.set_random_password()

    def clear_form(self) -> None:
        for i in [
            self.name,
            self.password,
            self.photo_directory
        ]:
            i.clear()
        self.set_random_password()

    def check_input_box(self) -> bool:
        name = self.name.get().strip()
        password = self.password.get().strip()
        photo_directory = self.photo_directory.get()
        # Empty
        if not name:
            messagebox.showerror('Name Error', 'Name cannot be empty!')
            return False
        elif not password:
            messagebox.showerror('Password Error', 'Password cannot be empty!')
            return False
        elif not photo_directory:
            messagebox.showerror('Photo Directory Error', 'Photo Directory cannot be empty!')
            return False

        is_good_password, error_messages = input_checking.is_valid_password(password)
        if not is_good_password:
            tk.messagebox.showerror(title='Password Error', message=error_messages)
            return False

    def submit_form(self) -> dict:
        if self.check_input_box():
            name = self.name.get().strip()
            password = self.password.get().strip()
            photo_directory = self.photo_directory.get()
            return {"name": name, "password": password, "photo": photo_directory}

    def set_random_password(self) -> None:
        password = password_management.generate_valid_password()
        self.password.set(password)

    def select_all(self, event) -> None:
        self.password.entry.select_range(0, tk.END)


class ButtonFrame(tk.Frame):
    def __init__(self, master: tk.Frame, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.btn_clear = tk.Button(self, text='Clear')
        self.btn_clear.pack(side=tk.LEFT)

        self.btn_submit = tk.Button(self, text='Submit')
        self.btn_submit.pack(side=tk.LEFT)

        self.pack()

    def set_callback(self, clear: callable, submit: callable):
        self.btn_clear.config(command=clear)
        self.btn_submit.config(command=submit)


class ShowAccountsView(View):
    def __init__(self, master: tk.ttk) -> None:
        super().__init__(master)
        master.title('Password Management UI - Show Accounts Page')
        self.master = master
        self.accounts = tk.Frame(self.master)
        self.accounts.pack(side=tk.TOP)
        self.display_accounts()

    def display_accounts(self):
        accounts = core.get_accounts()
        tk.Label(self.accounts, text=f'There are {len(accounts)} accounts').pack(side=tk.TOP)
        for account in accounts:
            tk.Label(self.accounts, text=account).pack()


class RegisterView(View):
    def __init__(self, master: ttk) -> None:
        super().__init__(master)
        master.title('Register')
        self.master = master
        self.form = Form(self.master)
        # self._frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=PADDING, pady=PADDING)
        self.button_frame = ButtonFrame(self.master)

        self.button_frame.set_callback(
            clear=self.form.clear_form,
            submit=self.form.submit_form
        )
        self.form.set_random_password()


class LoginView(View):
    def __init__(self, master: ttk) -> None:
        super().__init__(master)
        master.title('Login')
        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.TOP)
        self.username = Row(self.frame, 'Username')
        self.password = PasswordRow(self.frame, 'Password')
        # self.password.entry.config(show='*')

        tk.Button(self.frame, text='Login', width=10, command=self.login).pack()

    def login(self) -> bool:
        username = self.username.get()
        password = self.password.get()
        if not username:
            tk.messagebox.showerror('Name Error', 'Name cannot be empty!')
            return False
        elif not password:
            tk.messagebox.showerror('Password Error', 'Password cannot be empty!')
            return False

        if username in core.password_database:
            record = core.password_database[username]
            if validate_password(
                    raw_string=password,
                    salt=record['salt'],
                    key=record['private_key'],
                    stored_password=record['password']
            ):
                program = facial_recognition.FacialRecognition(FACES_DIRECTORY)
                if program.recognize_face(username):
                    tk.messagebox.showinfo('Welcome', f'Welcome, {username}')
        else:
            tk.messagebox.showinfo('Error', 'Login failed')


def new_login_window() -> None:
    create_new_window(LoginView)


def new_register_window() -> None:
    create_new_window(RegisterView)


def new_show_accounts() -> None:
    create_new_window(ShowAccountsView)


def create_new_window(new_page_class: callable) -> None:
    new_window = tk.Toplevel()
    new_page_class(new_window)


def main():
    Main()


if __name__ == '__main__':
    main()
