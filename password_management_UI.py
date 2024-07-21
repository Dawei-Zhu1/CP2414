"""
This python program is a collection of previous tasks to build a password manage system.
By Zhu Dawei
"""
import os.path
import shutil

import password_management
from password_management import *

import facial_recognition
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

PADDING = 10
LABEL_WIDTH = 10


class Row(tk.Frame):
    """
    Generate row like:
    [Label] [Input box]
    """

    def __init__(self, master: tk.Frame, label, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.label = tk.Label(self, text=label, width=LABEL_WIDTH, anchor=tk.W)
        self.label.pack(side=tk.LEFT)
        self.entry = tk.Entry(self)
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


class RowForPhoto(Row):
    def __init__(self, master: tk.Frame, label, **kwargs):
        super().__init__(master, label, **kwargs)
        self.select_photo_btn = tk.Button(self, text='Select...')
        self.select_photo_btn.pack(side=tk.LEFT)


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
        elif not password:
            messagebox.showerror('Password Error', 'Password cannot be empty!')
        elif not photo_directory:
            messagebox.showerror('Photo Directory Error', 'Photo Directory cannot be empty!')
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


class WelcomeFrame():
    def __init__(self, master: tk.ttk, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        master.title('Password Management UI')

        # self.button_frame = ButtonFrame(master)


class PasswordManagementUI:
    def __init__(self, master: ttk) -> None:
        master.title('Register')

        self.master = master
        self.core = PasswordManagement()
        self.form = Form(self.master)
        # self._frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=PADDING, pady=PADDING)
        self.button_frame = ButtonFrame(self.master)

        self.button_frame.set_callback(
            clear=self.form.clear_form,
            submit=self.form.submit_form
        )
        self.form.set_random_password()


def encapsulate(root: tk.Tk) -> None:
    PasswordManagementUI(root)


def main():
    root = tk.Tk()
    encapsulate(root)
    root.mainloop()


if __name__ == '__main__':
    main()
