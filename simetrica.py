from cryptography.fernet import Fernet

# Gerar chave simétrica (usada para cifrar e decifrar)
key = Fernet.generate_key()
cipher = Fernet(key)

# Texto original
texto = "Exemplo de criptografia simétrica"

# Cifrar
cifrado = cipher.encrypt(texto.encode())
print("Texto Cifrado:", cifrado)

# Decifrar
decifrado = cipher.decrypt(cifrado).decode()
print("Texto Decifrado:", decifrado)

# Mostrar a chave (normalmente você salva isso em arquivo seguro)
print("Chave usada (simétrica):", key)
