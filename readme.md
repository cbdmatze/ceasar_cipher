

# Caesar Cipher Encryption & Decryption

This Python program implements the Caesar cipher for encrypting and decrypting text. It supports both uppercase and lowercase letters, spaces, punctuation, and special characters. The shift key can be positive (for forward shifts) or negative (for backward shifts).

## Features

- Encrypts and decrypts text using the Caesar cipher.
- Supports both lowercase and uppercase letters.
- Special characters (spaces, punctuation, etc.) remain unchanged.
- Allows customization of the shift key for encryption and decryption.

## How the Caesar Cipher Works

The Caesar cipher is a type of substitution cipher where each letter in the text is shifted by a certain number of positions (defined by the **key**) in the alphabet. For example, with a key of 3:
- 'a' becomes 'd'
- 'b' becomes 'e'
- 'z' wraps around and becomes 'c'

Similarly, for decryption, the letters are shifted back by the same number of positions.

### Example:
Encrypting "Learning Python is Fun!" with a key of 3 will result in:
```
Encrypted: "Ohduqlqj Sbwkrq lv Ixq!"
```

Decrypting the same text will return the original:
```
Decrypted: "Learning Python is Fun!"
```

## Program Structure

The main functions in this program are:

### `encrypt_char(char, key)`
Encrypts a single character using the Caesar cipher.

### `encrypt_caesar(text, key)`
Encrypts a full string of text using the Caesar cipher, keeping special characters and spaces unchanged.

### `decrypt_char(char, key)`
Decrypts a single character that was encrypted using the Caesar cipher.

### `decrypt_caesar(ciphertext, key)`
Decrypts an encrypted string (ciphertext) and returns the original text.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone the repository or download the script files.
2. Navigate to the directory containing the script.

To run the program, simply execute:

```bash
python caesar.py
```

By default, the program contains example usage in the `main()` function that demonstrates both encryption and decryption with a sample text.

### Example Code Usage

In the `main()` function, you will find the following examples:

```python
def main():
    # Example usage of the encryption function
    text_to_encrypt = 'Learning Python is Fun!'
    shift_key = 3
    encrypted_text = encrypt_caesar(text_to_encrypt, shift_key)
    print(f"Encrypted: '{encrypted_text}'")  # Output: 'Ohduqlqj Sbwkrq lv Ixq!'

    # Example usage of the decryption function
    ciphertext = 'Ohduqlqj Sbwkrq lv Ixq!'
    decrypted_text = decrypt_caesar(ciphertext, shift_key)
    print(f"Decrypted: '{decrypted_text}'")  # Output: 'Learning Python is Fun!'
```

#### Encrypting Text

To encrypt text, you can call the `encrypt_caesar` function with the desired string and key. For example:
```python
encrypted = encrypt_caesar("Hello World!", 5)
print(encrypted)  # Output: "Mjqqt Btwqi!"
```

#### Decrypting Text

To decrypt the encrypted text, use the `decrypt_caesar` function with the ciphertext and the key:
```python
decrypted = decrypt_caesar("Mjqqt Btwqi!", 5)
print(decrypted)  # Output: "Hello World!"
```

## Customization

You can modify the `main()` function to encrypt and decrypt any text you'd like by changing the input `text_to_encrypt` and the `shift_key`.

## License

This project is open source and available under the [MIT License](LICENSE).

---

### Example Output

Here's an example of how the program works when running with the built-in example:

```bash
$ python caesar.py
Encrypted: 'Ohduqlqj Sbwkrq lv Ixq!'
Decrypted: 'Learning Python is Fun!'
```

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue!
