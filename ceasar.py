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
        original_position = ord(char) - ord('a')  # Get position in range 0-25
        shifted_position = (original_position + key) % 26  # Shift and wrap around using modulo
        encrypted_char = chr(shifted_position + ord('a'))  # Convert back to character
    elif 'A' <= char <= 'Z':
        original_position = ord(char) - ord('A')  # Get position in range 0-25
        shifted_position = (original_position + key) % 26  # Shift and wrap around using modulo
        encrypted_char = chr(shifted_position + ord('A'))  # Convert back to character
    else:
         # If the caracter is not a letter, return it unchanged 
         encrypted_char = char

    return encrypted_char

def encrypt_caesar(text, key):
    """
    Encrypts a string of letters using the Caesar cipher, supporting both
    lowercase and uppercase letters.

    Parameters:
        text (str): A string containing only letters (a-z, A-Z).
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
        original_position = ord(char) - ord('a')  # Get position in range 0-25
        shifted_position = (original_position - key) % 26  # Shift back and wrap around using modulo
        decrypted_char = chr(shifted_position + ord('a'))  # Convert back to character
    elif 'A' <= char <= 'Z':
        original_position = ord(char) - ord('A')  # Get position in range 0-25
        shifted_position = (original_position - key) % 26  # Shift back and wrap around using modulo
        decrypted_char = chr(shifted_position + ord('A'))  # Convert back to character
    else:
        # If char is not a letter, return it unchanged
        decrypted_char = char

    return decrypted_char

def decrypt_caesar(ciphertext, key):
    """
    Decrypts a string of letters using the Caesar cipher, supporting both
    lowercase and uppercase letters.

    Parameters:
        ciphertext (str): A string containing the encrypted text (a-z, A-Z).
        key (int): The shift key for the Caesar cipher.

    Returns:
        str: The decrypted string after applying the Caesar shift.
    """
    decrypted_text = ''.join(decrypt_char(char, key) for char in ciphertext)
    return decrypted_text


if __name__ == "__main__":
    # Encryption
    encrypted_text = encrypt_caesar('LearniNg', 3)
    print(encrypted_text)  # Output: 'OhduqlQj'

    # Decryption
    decrypted_text = decrypt_caesar('OhduqlQj', 3)
    print(decrypted_text)  # Output: 'LearniNg'
