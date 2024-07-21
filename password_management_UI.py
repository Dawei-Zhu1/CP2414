"""
This python program is a collection of previous tasks to build a password manage system.
By Zhu Dawei
"""
import os.path
import shutil

from password_management import *

import facial_recognition
import tkinter as tk
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
        self.pack(fill=tk.BOTH, expand=True)

    def clear(self):
        """
        Clear the text box
        """
        self.entry.delete(0, tk.END)

    def get(self):
        """
        Return the text
        """
        return self.entry.get()


class Form(tk.Frame):
    def __init__(self, master: tk.Frame, **kwargs):
        super().__init__(master, height=100, width=200, **kwargs)
        self._master = master

        self._frame = tk.Frame(self)
        self._frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.name = Row(self._master, 'Name')
        self.password = Row(self._master, 'Password')
        self.photo_directory = Row(self._master, 'Your photo')

    def clear_form(self):
        for i in [
            self.name,
            self.password,
            self.photo_directory
        ]:
            i.clear()

    def submit_form(self) -> dict:
        return {"name": self.name, "password": self.password, "photo": self.photo_directory}


class ButtonFrame(tk.Frame):
    def __init__(self, master: tk.Frame, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.frame = tk.Frame(self, padx=PADDING, pady=PADDING)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.btn_clear = tk.Button(text='Clear')
        self.btn_clear.pack(side=tk.LEFT)

        self.btn_submit = tk.Button(text='Submit')
        self.btn_submit.pack(side=tk.LEFT)

    def set_callback(self, clear: callable, submit: callable):
        self.btn_clear.config(command=clear)
        self.btn_submit.config(command=submit)


class PasswordManagementUI:
    def __init__(self, master: ttk) -> None:
        master.title('Password Management UI')

        self.master = master
        self.core = PasswordManagement()
        self.frame = Form(self.master)
        # self._frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=PADDING, pady=PADDING)
        self.button_frame = ButtonFrame(self.master)

        self.button_frame.set_callback(
            clear=self.frame.clear_form,
            submit=self.frame.submit_form
        )


def encapsulate(root: tk.Tk) -> None:
    PasswordManagementUI(root)


def main():
    root = tk.Tk()
    encapsulate(root)
    root.mainloop()


if __name__ == '__main__':
    main()
