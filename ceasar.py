def encrypt_char(char, key):
    """
    Encrypts a single character using the Caesar cipher, supporting both
    lowercase and uppercase letters.

    Parameters:
        char (str): A single character to encrypt (a-z, A-Z).
        key (int): The shift key for the Caesar cipher.

    Returns:
        str: The encrypted character after applying the Caesar shift.
    """
    if 'a' <= char <= 'z':
        original_position = ord(char) - ord('a')
        shifted_position = (original_position + key) % 26
        encrypted_char = chr(shifted_position + ord('a'))
    elif 'A' <= char <= 'Z':
        original_position = ord(char) - ord('A')
        shifted_position = (original_position + key) % 26
        encrypted_char = chr(shifted_position + ord('A'))
    else:
        # If the character is not a letter, return it unchanged
        encrypted_char = char

    return encrypted_char

def encrypt_caesar(text, key):
    """
    Encrypts a string of letters and supports special characters
    using the Caesar cipher.

    Parameters:
        text (str): A string containing letters (a-z, A-Z) and special characters.
        key (int): The shift key for the Caesar cipher.

    Returns:
        str: The encrypted string after applying the Caesar shift.
    """
    encrypted_text = ''.join(encrypt_char(char, key) for char in text)
    return encrypted_text

def decrypt_char(char, key):
    """
    Decrypts a single character using the Caesar cipher, supporting both
    lowercase and uppercase letters.

    Parameters:
        char (str): A single character to decrypt (a-z, A-Z).
        key (int): The shift key for the Caesar cipher.

    Returns:
        str: The decrypted character after applying the Caesar shift.
    """
    if 'a' <= char <= 'z':
        original_position = ord(char) - ord('a')
        shifted_position = (original_position - key) % 26
        decrypted_char = chr(shifted_position + ord('a'))
    elif 'A' <= char <= 'Z':
        original_position = ord(char) - ord('A')
        shifted_position = (original_position - key) % 26
        decrypted_char = chr(shifted_position + ord('A'))
    else:
        # If the character is not a letter, return it unchanged
        decrypted_char = char

    return decrypted_char

def decrypt_caesar(ciphertext, key):
    """
    Decrypts a string of letters and supports special characters
    using the Caesar cipher.

    Parameters:
        ciphertext (str): A string containing the encrypted text (a-z, A-Z).
        key (int): The shift key for the Caesar cipher.

    Returns:
        str: The decrypted string after applying the Caesar shift.
    """
    decrypted_text = ''.join(decrypt_char(char, key) for char in ciphertext)
    return decrypted_text

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

if __name__ == "__main__":
    main()
