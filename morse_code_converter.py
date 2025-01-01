morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.'
}

def morse_code_converter(message: str, decode: bool = False) -> str:
    """
    Converts a message to or from Morse code.
    
    Args:
    - message (str): The input message (plain text or Morse code).
    - decode (bool): If True, decodes Morse code to text; if False, encodes text to Morse code.
    
    Returns:
    - str: The converted message.
    """
    if decode:
        morse_to_text = {v: k for k, v in morse_code_dict.items()}
        words = message.strip().split(' / ')
        decoded_message = []
        for word in words:
            decoded_message.append(
                ''.join(morse_to_text.get(code, '') for code in word.split())
            )
        return ' '.join(decoded_message)
    else:
        text = message.upper()
        encoded_message = []
        for char in text:
            if char == ' ':
                encoded_message.append('/')
            else:
                encoded_message.append(morse_code_dict.get(char, ''))
        return ' '.join(encoded_message).strip()

choice = input("Do you want to encode or decode? (e/d): ").lower()
message = input("Enter your message: ")

match choice :
    case 'e':
        print("Encoded message:", morse_code_converter(message, decode=False))  
    case 'd':
        print("Decoded message:", morse_code_converter(message, decode=True))
    case _ :
        print("Invalid choice. Please choose 'e' to encode or 'd' to decode.")
