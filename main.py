"""
Simple Morse Code Converter (Text -> Morse).

Features (Current):
  1. Displays an ASCII art welcome banner at startup.
  2. Prompts the user for text input repeatedly.
  3. Converts the input text to Morse code.
     - Uses a hard-coded word separator ('/').
     - Unknown characters are replaced by '???'.
  4. Prints the result, along with a common Morse prosign (... -.-) for end of contact.
  5. Continues until the user chooses to quit.
  6. Displays a goodbye ASCII art message upon exit.

TODO (Future Enhancements):
  - Implement reverse conversion (Morse -> Text).

"""

from morse_code_converter.ascii_art import AsciiArt
from morse_code_converter.morse_code import MorseCodeConverter

def main():
    """
    Main entry point of the application. Coordinates:
      - Welcome ASCII art
      - Input loop for text
      - Conversion to Morse
      - Printing the result
      - Goodbye ASCII art

    TODO: Integrate an optional reverse mode in a future commit.
    """
    # 1. Display a welcome ASCII art banner
    AsciiArt.display_welcome_art()

    while True:
        # 2. Prompt for user input (text)
        user_text = input("Type your message here: ").strip()

        # 3. Convert from text to Morse (no argparse; hard-coded defaults)
        morse = MorseCodeConverter.string_to_morse(
            input_string=user_text,
            word_separator="/",      # Hard-coded word separator
            unknown_strategy="???"   # Replace unrecognized chars with ???
        )

        # 4. Print the Morse code result
        print("\nConversion Result:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(morse)
        print("... -.- (SK)")  # Prosign indicating end of communication
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        # 5. Ask if the user wants to continue
        again = input("Do you want to convert another message? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            # 6. Display a goodbye ASCII art message and exit
            AsciiArt.display_goodbye_art()
            break


if __name__ == "__main__":
    main()