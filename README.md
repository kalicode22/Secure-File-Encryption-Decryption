**# Secure File Encryption/Decryption**

This Python script enables secure encryption and decryption of files using AES encryption with PBKDF2 key derivation. It utilizes the `cryptography` library for cryptographic operations.

## Features

- **Encryption**: Encrypts a file with a user-provided password.
- **Decryption**: Decrypts an encrypted file using the original password.

## Requirements

- Python 3.x
- `cryptography` library (`pip install cryptography`)

## Installation

1. Clone the repository or download the `file_crypto.py` script.

   ```bash
   git clone <repository_url>
   cd secure_file_crypto
   ```

2. Install the required dependencies.

   ```bash
   pip install cryptography
   ```

## Usage

### Encryption

To encrypt a file:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `file_crypto.py`.
3. Run the script and follow the prompts:
   
   ```bash
   python file_crypto.py
   ```
   
   - Enter `E` when prompted for encryption.
   - Provide the path to the file you want to encrypt.
   - Enter a strong password for encryption.

   Example:
   ```bash
   Enter 'E' for encryption or 'D' for decryption: E
   Enter the path of the file to encrypt: /path/to/your/file.txt
   Enter the password for encryption: YourStrongPassword
   ```

4. The encrypted file will be created in the same directory with `.enc` extension appended to the original filename.

### Decryption

To decrypt an encrypted file:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `file_crypto.py`.
3. Run the script and follow the prompts:
   
   ```bash
   python file_crypto.py
   ```
   
   - Enter `D` when prompted for decryption.
   - Provide the path to the encrypted file (`filename.enc`).
   - Enter the password used for encryption.

   Example:
   ```bash
   Enter 'E' for encryption or 'D' for decryption: D
   Enter the path of the file to decrypt: /path/to/your/encrypted_file.enc
   Enter the password for decryption: YourStrongPassword
   ```

4. The decrypted file will be created in the same directory with `_decrypted` appended to the original filename.

## Notes

- Ensure to keep your password secure and confidential.
- Test the encryption and decryption process with sample files before using it on sensitive data.
- For advanced usage or customization, refer to the `cryptography` library documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

### Instructions for Use

1. **Description**: Provide an overview of what the project does, its main features, and its purpose.
   
2. **Requirements**: List any dependencies or prerequisites needed to run the project, including installation instructions.

3. **Installation**: Instructions on how to install the project, including downloading and setting up dependencies.

4. **Usage**:
   - **Encryption**: Step-by-step instructions on how to encrypt a file using the script, including prompts and example commands.
   - **Decryption**: Step-by-step instructions on how to decrypt an encrypted file, including prompts and example commands.

5. **Notes**: Additional tips or considerations for using the project effectively and securely.

6. **License**: Specify the project's licensing information.

This README file provides clear instructions for users to effectively utilize your Secure File Encryption/Decryption project, ensuring they can encrypt and decrypt files securely with ease. Adjust the paths and commands based on your project's directory structure and specific implementation details.
