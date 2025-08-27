from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

# Gerar par de chaves RSA (privada e pública)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Texto original
texto = b"Exemplo de criptografia assimétrica"

# Cifrar com chave pública
cifrado = public_key.encrypt(
    texto,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Texto Cifrado:", cifrado)

# Decifrar com chave privada
decifrado = private_key.decrypt(
    cifrado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Texto Decifrado:", decifrado.decode())
