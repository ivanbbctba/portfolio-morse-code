"""
Simple Morse Code Converter (Text -> Morse).

Features:
  1. Displays an ASCII art welcome banner at startup.
  2. Lets the user choose one of two modes each time:
       - Text -> Morse
       - Morse -> Text
  3. Prompts the user for input repeatedly.
  4. Converts the input using either:
       - string_to_morse (with default '/' separator and ??? for unknown chars), or
       - morse_to_string (with the same defaults).
  5. Prints the result, with a special note for text->Morse (... -.-).
  6. Continues until the user chooses to quit.
  7. Displays a goodbye ASCII art message upon exit.

"""

from morse_code_converter.ascii_art import AsciiArt
from morse_code_converter.morse_code import MorseCodeConverter


def main():
    """
    Main entry point of the application. Coordinates:
      - Welcome ASCII art
      - Mode selection (Text->Morse or Morse->Text)
      - Conversion
      - Printing the result
      - Goodbye ASCII art
    """
    # 1. Display a welcome ASCII art banner
    AsciiArt.display_welcome_art()

    while True:
        # Ask the user which conversion mode they want
        mode = input(
            "Which conversion do you want? "
            "[T] for Text -> Morse, [M] for Morse -> Text: "
        ).strip().lower()

        if mode == "t":
            # TEXT -> MORSE
            user_text = input("\nType your message here: ").strip()
            converted = MorseCodeConverter.string_to_morse(
                input_string=user_text,
            )
            print("\nConversion Result (Text -> Morse):")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(converted)
            print("... -.- (SK)")  # Prosign indicating end of communication
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        elif mode == "m":
            # MORSE -> TEXT
            user_morse = input("\nType your Morse code here: ").strip()
            converted = MorseCodeConverter.morse_to_string(
                morse_code=user_morse,
            )
            print("\nConversion Result (Morse -> Text):")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(converted)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

        else:
            print("Invalid option. Please type 'T' or 'M'.\n")
            continue  # Ask again without dropping into the exit prompt

        # Ask if the user wants to continue
        again = input("Do you want to do another conversion? (y/n): ").strip().lower()
        if again not in ["y", "yes"]:
            # Display a goodbye ASCII art message and exit
            AsciiArt.display_goodbye_art()
            break


if __name__ == "__main__":
    main()