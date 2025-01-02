"""Graphic Interface"""
import tkinter as tk
from tkinter import messagebox
from log_sign import LogSign


class Gui:
    """Graphic Interface"""

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Log in")
        self.ventana.geometry("250x220")
        self.ventana.resizable(0, 0)

        self.log_sign_manager = LogSign()

        self.username_frame = tk.Frame(self.ventana)
        self.username_frame.pack(pady=10)

        self.username_label = tk.Label(self.username_frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.username_frame)
        self.username_entry.pack()

        self.password_frame = tk.Frame(self.ventana)
        self.password_frame.pack(pady=10)

        self.password_label = tk.Label(self.password_frame, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.password_frame, show='*')
        self.password_entry.pack()

        self.varcon_showpassword = tk.BooleanVar()
        self.show_password = tk.Checkbutton(
            self.ventana, text="Show password", command=self.toggle_show_password, variable=self.varcon_showpassword)
        self.show_password.pack()

        self.login_button = tk.Button(
            self.ventana, text="Log in", command=self.log_in, height=1, width=8, font="Arial 12")
        self.login_button.pack(pady=5)

        self.singup_button = tk.Button(
            self.ventana, text="Sing up", font="Arial 8", command=self.show_sign_up)
        self.singup_button.pack(pady=5)

    def show_sign_up(self):
        """Create the root for sign up"""
        self.ventana.destroy()
        self.ventana = tk.Tk()
        self.ventana.title("Sign up")
        self.ventana.resizable(0, 0)

    def get_username(self):
        """Return the content of the username entry"""
        return self.username_entry.get()

    def get_password(self):
        """Return the content of the password entry"""
        return self.password_entry.get()

    def log_in(self):
        """Log in"""
        can_login, message = self.log_sign_manager.log_in(
            self.get_username(), self.get_password())
        if can_login:
            messagebox.showinfo(title="Log in", message=message)
        else:
            messagebox.showwarning(title="Log in", message=message)

    def toggle_show_password(self):
        """Toggle to show or not the password"""
        toggle = self.varcon_showpassword.get()
        self.password_entry.config(show='' if toggle else '*')

    def start(self):
        """Start the root"""
        self.ventana.mainloop()
