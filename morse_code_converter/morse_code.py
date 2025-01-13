"""
This module contains the logic for converting strings to Morse code and vice versa.
Includes error handling, logging, and customizable behaviors.
"""

import logging

# Configure a basic logger (could configure more advanced handlers, levels, etc.)
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(message)s'
)


class MorseCodeConverter:
    """
    A class-based Morse Code Converter with:
      - string_to_morse: Convert text to Morse
      - morse_to_string: Convert Morse to text
      - Customizable unknown character handling
      - Configurable word separator
    """

    DEFAULT_UNKNOWN_STR = "???"

    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
        'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
        '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }

    @staticmethod
    def string_to_morse(
            input_string: str,
            word_separator: str = '/',
            unknown_strategy: str = '???'
    ) -> str:
        """
        Converts a string to Morse code.

        :param input_string: Text to be converted
        :param word_separator: String used to separate words in Morse (default '/')
        :param unknown_strategy: String to use for unknown characters, or "ignore" to skip them
        :return: Morse code representation of the input string
        """
        input_string = input_string.strip().upper()

        morse_output = []
        for char in input_string:
            if char == " ":
                morse_output.append(word_separator)
            elif char in MorseCodeConverter.MORSE_CODE_DICT:
                morse_output.append(MorseCodeConverter.MORSE_CODE_DICT[char])
            else:
                if unknown_strategy.lower() == "ignore":
                    logging.debug(f"Ignoring unknown character: {char}")
                    continue
                else:
                    logging.warning(f"Unknown character encountered: {char}")
                    morse_output.append(unknown_strategy)

        return " ".join(morse_output)

    @staticmethod
    def morse_to_string(
            morse_code: str,
            word_separator: str = '/',
            unknown_strategy: str = '???'
    ) -> str:
        """
        Converts Morse code back to a text string.

        :param morse_code: The Morse code string to convert
        :param word_separator: String used to separate words in Morse (default '/')
        :param unknown_strategy: String to insert for unknown Morse patterns, or "ignore" to skip them
        :return: Decoded text from the Morse code
        """
        # Build a reverse lookup dictionary for quick decoding
        reverse_dict = {v: k for k, v in MorseCodeConverter.MORSE_CODE_DICT.items()}

        # Split on spaces to get individual Morse "letters" or word separators
        morse_tokens = morse_code.split()

        decoded_chars = []
        for token in morse_tokens:
            if token == word_separator:
                # We’ll treat word separator as an actual space
                decoded_chars.append(" ")
            elif token in reverse_dict:
                decoded_chars.append(reverse_dict[token])
            else:
                if unknown_strategy.lower() == "ignore":
                    logging.debug(f"Ignoring unknown Morse pattern: {token}")
                    continue
                else:
                    logging.warning(f"Unknown Morse pattern encountered: {token}")
                    decoded_chars.append(unknown_strategy)

        # Combine decoded characters, then collapse multiple spaces
        decoded_string = "".join(decoded_chars)
        # You could refine spacing logic if you wish
        return " ".join(decoded_string.split())
