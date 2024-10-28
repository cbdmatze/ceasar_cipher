def encrypt_char(char, key):
    """
    Encrypts a single character using the Ceasar cipher.
    
    Parameters:
        char (str): A single character to encrypt (a-z).
        key (int): The shift key for the Ceasar cipher.
        
    Returns:
        str: The encrypted character after applying the Ceasar shift.
    """
    # Ensure the character is within 'a' to 'z'
    if not ('a' <= char <= 'z'):
        raise ValueError("character must be a lowercase letter a-z")
    
    # Calculate the shifted position
    original_position = ord(char) - ord('a') # Get position in range 0 - 25
    shifted_position = (original_position + key) % 26 # Shift and wrap around using modulo
    enchrypted_char = chr(shifted_position + ord('a')) # Convert back to character

    return enchrypted_char


if __name__ == "__main__":
    print(encrypt_char('a', 3))  # Output: 'd'
    print(encrypt_char('b', 3))  # Output: 'e'
    print(encrypt_char('a', -2))  # Output: 'y'
