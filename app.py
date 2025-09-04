import bcrypt
import sqlite3

# Ejemplo con SQLite para simplificar
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Usuario: ")
password = input("Contraseña: ")

cursor.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
row = cursor.fetchone()

if row:
    user_id, stored_hash = row
    if bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8")):
        print("Login exitoso ✅")
    else:
        print("Credenciales inválidas ❌")
else:
    print("Credenciales inválidas ❌")
