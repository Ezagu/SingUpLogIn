"""Graphic Interface"""
import tkinter as tk
from tkinter import messagebox
from log_sign import LogSign


class Gui:
    """Graphic Interface"""

    def __init__(self):

        self.log_sign_manager = LogSign()

        self.ventana = tk.Tk()
        self.ventana.title("Log in")
        self.ventana.geometry("250x220")
        self.ventana.resizable(0, 0)

        self.username_entry = None
        self.password_entry = None
        self.username_entry_sign_up = None
        self.email_entry_sign_up = None
        self.password_entry_sign_up = None
        self.repeated_password_entry_sign_up = None
        self.ventana_sign_up = None

        self.create_login_window()

    def create_login_window(self):
        """Create the window for log in"""
        username_frame = tk.Frame(self.ventana)
        username_frame.pack(pady=10)

        username_label = tk.Label(username_frame, text="Username or email:")
        username_label.pack()
        self.username_entry = tk.Entry(username_frame)
        self.username_entry.pack()

        password_frame = tk.Frame(self.ventana)
        password_frame.pack(pady=10)

        password_label = tk.Label(password_frame, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(password_frame, show='*')
        self.password_entry.pack()

        self.varcon_showpassword = tk.BooleanVar()
        self.show_password = tk.Checkbutton(
            self.ventana, text="Show password", command=self.toggle_show_password,
            variable=self.varcon_showpassword)
        self.show_password.pack()

        login_button = tk.Button(
            self.ventana, text="Log in", command=self.log_in, height=1, width=8, font="Arial 12")
        login_button.pack(pady=5)

        singup_button = tk.Button(
            self.ventana, text="Sing up", font="Arial 8", command=self.create_signup_window)
        singup_button.pack(pady=5)

        self.ventana.mainloop()

    def create_signup_window(self):
        """Create the window for sign up"""

        self.ventana.withdraw()
        self.ventana_sign_up = tk.Toplevel(self.ventana)
        self.ventana_sign_up.title("Sign up")
        self.ventana_sign_up.geometry("250x260")
        self.ventana_sign_up.resizable(0, 0)

        username_label_sign_up = tk.Label(
            self.ventana_sign_up, text="Username:")
        username_label_sign_up.pack(pady=5)
        self.username_entry_sign_up = tk.Entry(self.ventana_sign_up)
        self.username_entry_sign_up.pack()

        email_label_sign_up = tk.Label(
            self.ventana_sign_up, text="Email:")
        email_label_sign_up.pack(pady=5)
        self.email_entry_sign_up = tk.Entry(self.ventana_sign_up)
        self.email_entry_sign_up.pack()

        password_label_sign_up = tk.Label(
            self.ventana_sign_up, text="Password:")
        password_label_sign_up.pack(pady=5)
        self.password_entry_sign_up = tk.Entry(self.ventana_sign_up, show='*')
        self.password_entry_sign_up.pack()

        repeated_password_label_sign_up = tk.Label(
            self.ventana_sign_up, text="Repeat the password:")
        repeated_password_label_sign_up.pack(pady=5)
        self.repeated_password_entry_sign_up = tk.Entry(
            self.ventana_sign_up, show='*')
        self.repeated_password_entry_sign_up.pack()

        button_frame = tk.Frame(self.ventana_sign_up)
        button_frame.pack()

        signup_button = tk.Button(
            button_frame, text="Sign up", command=self.sign_up)
        signup_button.pack(side="left", padx=3, pady=10)

        cancel_button = tk.Button(
            button_frame, text="Cancel", command=self.close_sign_up)
        cancel_button.pack(side="left", padx=3, pady=10)

    def log_in(self):
        """Log in"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        can_login, message = self.log_sign_manager.log_in(
            username, password)

        if can_login:
            messagebox.showinfo(title="Log in", message=message)
        else:
            messagebox.showwarning(title="Log in", message=message)

    def sign_up(self):
        """Sign up"""
        password = self.password_entry_sign_up.get()
        repeated_password = self.repeated_password_entry_sign_up.get()
        email = self.email_entry_sign_up.get()
        username = self.username_entry_sign_up.get()

        if not username or not email or not password or not repeated_password:
            messagebox.showwarning(
                title="Sign up", message="Error al crear usuario:\nFalta ingresar datos")
            return

        if password != repeated_password:
            messagebox.showwarning(title="Sign up",
                                   message="Error al crear usuario:\nLas contraseñas no coinciden")
            return

        if '@' not in email:
            messagebox.showwarning(title="Sign up",
                                   message="Error al crear usuario:\nMail no válido")
            return

        can_signup, message = self.log_sign_manager.sign_up(
            username, email, password)

        if can_signup:
            messagebox.showinfo(
                title="Sign up", message="Se creó el usuario correctamente")
            self.close_sign_up()
        else:
            messagebox.showwarning(title="Sign up",
                                   message=f"Error al crear el usuario: \n{message}")

    def close_sign_up(self):
        """Close the window of the sign up and show the login window"""
        if self.ventana_sign_up:
            self.ventana_sign_up.destroy()
        self.ventana.deiconify()

    def toggle_show_password(self):
        """Toggle to show or not the password"""
        toggle = self.varcon_showpassword.get()
        self.password_entry.config(show='' if toggle else '*')
