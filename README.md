# Morse Code Converter

A Python program to encode text into Morse code and decode Morse code back into text. This tool is simple, flexible, and easily extendable, allowing users to add more characters to the Morse code dictionary.

## Features

- **Encode**: Convert text to Morse code.
- **Decode**: Convert Morse code back to text.
- **Customizable**: Easily expand the Morse code dictionary with additional letters, numbers, or symbols.

## How It Works

- **Encoding**: Each character in the input text is mapped to its corresponding Morse code value. Words are separated by `/` in the encoded output.
- **Decoding**: The Morse code input is split by spaces for letters and `/` for words. Each Morse code sequence is translated back to its original character.

## Usage

### Prerequisites

- Python 3.x installed on your system.

### Running the Program

1. Clone or download this repository to your local machine.
2. Run the script using Python:

   ```bash
   python morse_code_converter.py
   ```

3. Choose whether to encode or decode:
   - Enter **`e`** to encode text to Morse code.
   - Enter **`d`** to decode Morse code to text.

4. Input your message and get the result.

### Example

#### Encoding
Input:
```
Do you want to encode or decode? (e/d): e
Enter your message: Hello World
```

Output:
```
Encoded message: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

#### Decoding
Input:
```
Do you want to encode or decode? (e/d): d
Enter your message: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
```

Output:
```
Decoded message: HELLO WORLD
```

## Extending the Dictionary

To add more characters, expand the `morse_code_dict` in the code. For example:

```python
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    # Existing characters...
    '!': '-.-.--', '@': '.--.-.', '&': '.-...'  # Add more symbols here
}
```

Simply map the character to its Morse code equivalent.

## Notes

- Words are separated by `/` in Morse code for clarity.
- If the program encounters a character not in the dictionary, it will be ignored in the encoding process.

## Contributing

Feel free to fork this repository and submit pull requests to add new features or improve the code.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

Enjoy encoding and decoding with this Morse Code Converter!
