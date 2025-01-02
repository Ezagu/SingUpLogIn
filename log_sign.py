"""Connection with the database"""
import sqlite3
from bcrypt import hashpw, gensalt, checkpw


class LogSign:
    """Connection with the database"""

    def __init__(self):
        self.conn = sqlite3.connect("database.db")

    def log_in(self, username, password):
        """Return if the user is on the database"""
        query = '''
            SELECT password FROM users
            WHERE user_name = ?
        '''
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (username,))
            result = cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error al iniciar sesion: {e}")
            return False
        finally:
            cursor.close()

        if not result:
            print("Usuario no encontrado")
            return False
        else:
            if checkpw(password.encode(), result[0]):
                print("Correct log in")
                return True
            else:
                print("Contraseña incorrecta")
                return False

    def sign_up(self, username, email, password):
        """Update the database with the parameters, return if can be updated"""
        hashed_password = hashpw(password.encode(), gensalt())
        print()
        query = '''
            INSERT INTO users (user_name, email, password)
            VALUES (?, ?, ?)
            '''
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, (username, email, hashed_password))
            self.conn.commit()
            print("Usuario registrado")
        except sqlite3.IntegrityError:
            print("El usuario o el correo ya están registrados.")
        finally:
            cursor.close()
