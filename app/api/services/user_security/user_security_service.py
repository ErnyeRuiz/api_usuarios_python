from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64decode
import os

class UserSecurityService:
    __clave_secreta: str = 'hola'

    @staticmethod
    def desencriptar(texto_cifrado_base64: str) -> str:
        key = UserSecurityService.__obtener_clave_secreta.ljust(32, '0').encode()[:32] # Asegurar que la clave tenga 32 bytes (AES-256)
        iv = b'\x00' * 16

        cifrar = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend= default_backend()
        )

        desencriptor = cifrar.decryptor()

        texto_cifrado = b64decode(texto_cifrado_base64)
        texto_plano = desencriptor.update(texto_cifrado) + desencriptor.finalize()

        return texto_plano.decode()
    
    @classmethod
    def __obtener_clave_secreta(cls):
        return cls.__clave_secreta
    

# Ejemplo de uso
# clave_secreta = "miClaveSecreta123"  # ¡La misma que en Flutter!
# texto_cifrado = "KZ7Pj3k4R2M6TnQ9oLmN+w=="  # Ejemplo de texto cifrado desde Flutter

# texto_descifrado = desencriptar(texto_cifrado, clave_secreta)
# print("Texto descifrado:", texto_descifrado)  # Output: "clave_super_secreta_123"