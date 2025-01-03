"""Connection with the database"""
import sqlite3
import sys
from os import path
from bcrypt import hashpw, gensalt, checkpw


class LogSign:
    """Connection with the database"""

    def __init__(self):
        path_to_db = "database.db"
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            # Si se ejecuta en un .exe
            bundle_dir = path.abspath(path.dirname(__file__))
            path_to_db = path.join(bundle_dir, 'database.db')
        self.conn = sqlite3.connect(path_to_db)

    def log_in(self, username, password):
        """Return if the user is on the database and a message"""
        query = '''
            SELECT password FROM users
            WHERE user_name = ? OR email = ?
        '''
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (username, username))
            result = cursor.fetchone()
        except sqlite3.Error as e:
            return False, f"Error al iniciar sesion: {e}"
        finally:
            cursor.close()

        if not result:
            return False, "Usuario no encontrado"
        else:
            if checkpw(password.encode(), result[0]):
                return True, "Correct log in"
            else:
                return False, "Contraseña incorrecta"

    def sign_up(self, username, email, password):
        """Update the database with the parameters, return if can be updated an a message"""
        hashed_password = hashpw(password.encode(), gensalt())
        query = '''
            INSERT INTO users (user_name, email, password)
            VALUES (?, ?, ?)
            '''
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (username, email, hashed_password))
            self.conn.commit()
            cursor.close()
            return True, "Usuario registrado con éxito"
        except sqlite3.IntegrityError:
            cursor.close()
            return False, "El usuario o el correo ya están registrados"
