"❌✅"
import json
from cryptography.fernet import Fernet
def desencriptar():
    try:
        # Cargar la clave
        with open("env/private_keys/clave.key", "rb") as clave_file:
            clave = clave_file.read()

        # Cargar los datos encriptados
        with open("credenciales_encriptadas.json", "rb") as archivo_encriptado:
            datos_encriptados = archivo_encriptado.read()

        # Desencriptar
        fernet = Fernet(clave)
        datos_desencriptados = fernet.decrypt(datos_encriptados)

        # Convertir el string JSON a diccionario de Python
        credenciales = json.loads(datos_desencriptados.decode())

        print("✅Credenciales desencriptadas correctamente")
    except Exception as error_desencriptacion:
        print(f"❌ Ocurrio un error al intentar desencriptar las credenciales \
              Error:{error_desencriptacion}")
    return credenciales
