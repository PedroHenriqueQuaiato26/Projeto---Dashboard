from cryptography.fernet import Fernet

# Gera uma chave e a salva em um arquivo
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Carrega a chave de um arquivo
def load_key():
    return open("secret.key", "rb").read()

# Criptografa uma mensagem
def encrypt_message(message):
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

# Descriptografa uma mensagem
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

# Gera uma chave se ainda não existir
generate_key()

# Senha a ser criptografada
password = "postgres"

# Criptografa a senha
encrypted_password = encrypt_message(password)
print(f"Encrypted password: {encrypted_password}")

# Descriptografa a senha
decrypted_password = decrypt_message(encrypted_password)
print(f"Decrypted password: {decrypted_password}")
