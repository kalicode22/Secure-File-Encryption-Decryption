from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import tempfile

def encrypt_file(file_path, password):
    # Read data from the file
    with open(file_path, 'rb') as file:
        data = file.read()

    # Generate salt and iv
    salt = os.urandom(16)
    iv = os.urandom(16)

    # Derive key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password.encode())

    # Encrypt the data using AES in CTR mode
    cipher = Cipher(
        algorithm=algorithms.AES(key),
        mode=modes.CTR(iv),
    )
    encryptor = cipher.encryptor()
    ct_data = encryptor.update(data) + encryptor.finalize()

    # Write encrypted data along with salt and iv to a new file
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, 'wb') as file:
        file.write(salt)
        file.write(iv)
        file.write(ct_data)

    print(f"File encrypted successfully as: {encrypted_file_path}")

def decrypt_file(file_path, password):
    # Read salt, iv, and encrypted data from the file
    with open(file_path, 'rb') as file:
        salt = file.read(16)
        iv = file.read(16)
        enc_data = file.read()

    # Derive key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = kdf.derive(password.encode())

    # Decrypt the data using AES in CTR mode
    cipher = Cipher(
        algorithm=algorithms.AES(key),
        mode=modes.CTR(iv),
    )
    decryptor = cipher.decryptor()
    pt_data = decryptor.update(enc_data) + decryptor.finalize()

    # Write decrypted data to a new file
    decrypted_file_path = file_path.replace('.enc', '_decrypted')
    with open(decrypted_file_path, 'wb') as file:
        file.write(pt_data)

    print(f"File decrypted successfully as: {decrypted_file_path}")

# Main function to handle user input and choice
if __name__ == "__main__":
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()

    if choice == 'E':
        file_path = input("Enter the path of the file to encrypt: ")
        password = input("Enter the password for encryption: ")
        encrypt_file(file_path, password)
    elif choice == 'D':
        file_path = input("Enter the path of the file to decrypt: ")
        password = input("Enter the password for decryption: ")
        decrypt_file(file_path, password)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
