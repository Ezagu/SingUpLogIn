"""Graphic Interface"""
import tkinter as tk
from log_sign import LogSign


class Gui:
    """Graphic Interface"""

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Log in")
        self.ventana.geometry("250x250")
        self.ventana.resizable(0, 0)

        self.log_sign_manager = LogSign()

        self.title_label = tk.Label(
            self.ventana, text="Log in", font="Arial 12 bold")
        self.title_label.pack(pady=10)

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
        self.password_entry = tk.Entry(self.password_frame)
        self.password_entry.pack()

        self.login_button = tk.Button(
            self.ventana, text="Log in", command=self.log_in)
        self.login_button.pack(pady=5)

        self.singup_button = tk.Button(self.ventana, text="Sing up")
        self.singup_button.pack(pady=5)

    def get_username(self):
        """Return the content of the username entry"""
        return self.username_entry.get()

    def get_password(self):
        """Return the content of the password entry"""
        return self.password_entry.get()

    def log_in(self):
        """Log in"""
        if self.log_sign_manager.log_in(self.get_username(), self.get_password()):
            self.emergent_root("Success login")
        else:
            self.emergent_root("Could not log in")

    def emergent_root(self, text):
        """Create an emergent root with a text"""
        root = tk.Toplevel(self.ventana)
        root.title(" ")
        root.resizable(0, 0)

        label = tk.Label(root, text=text, font="Arial 16 bold")
        label.pack(padx=20, pady=20)

    def start(self):
        """Start the root"""
        self.ventana.mainloop()
