# ❌ Login inseguro: vulnerable a SQL Injection y sin hash de contraseñas
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Usuario: ")
password = input("Contraseña: ")

# Consulta directa: PELIGROSA
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)
row = cursor.fetchone()

if row:
    print("Login exitoso ✅ (pero inseguro)")
else:
    print("Credenciales inválidas ❌")
