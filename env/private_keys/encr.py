import json
from cryptography.fernet import Fernet

# Generar y guardar la clave secreta
clave = Fernet.generate_key()
with open("env/private_keys/clave.key", "wb") as clave_file:
    clave_file.write(clave)

# Leer el archivo JSON original
with open("env/private_keys/credenciales.json", "r") as json_file:
    datos = json_file.read()

# Encriptar los datos
fernet = Fernet(clave)
datos_encriptados = fernet.encrypt(datos.encode())

# Guardar los datos encriptados en un archivo nuevo
with open("credenciales_encriptadas.json", "wb") as archivo_encriptado:
    archivo_encriptado.write(datos_encriptados)

print("✅ Credenciales encriptadas correctamente.")
