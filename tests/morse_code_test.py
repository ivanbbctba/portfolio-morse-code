import unittest
from morse_code_converter.morse_code import MorseCodeConverter


class TestMorseCodeConverter(unittest.TestCase):

    def test_simple_text(self):
        """
        Test a simple word like 'hello' -> Morse.
        """
        self.assertEqual(
            MorseCodeConverter.string_to_morse("hello"),
            ".... . .-.. .-.. ---"
        )

    def test_capitalization(self):
        """
        Test that capitalization doesn't affect the result.
        """
        self.assertEqual(
            MorseCodeConverter.string_to_morse("Hello"),
            ".... . .-.. .-.. ---"
        )

    def test_numbers_and_punctuation(self):
        """
        Test numbers and punctuation like '123' and '?'.
        """
        self.assertEqual(
            MorseCodeConverter.string_to_morse("123?"),
            ".---- ..--- ...-- ..--.."
        )

    def test_spaces_between_words(self):
        """
        Test that spaces are replaced with '/' by default.
        """
        self.assertEqual(
            MorseCodeConverter.string_to_morse("HELLO WORLD"),
            ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        )

    def test_unrecognized_characters(self):
        """
        Test behavior with characters not in the dictionary (using ???).
        """
        self.assertEqual(
            MorseCodeConverter.string_to_morse("@#$"),
            "??? ??? ???"
        )

    def test_reverse_conversion(self):
        """
        Test Morse -> text conversion.
        """
        morse = ".... . .-.. .-.. ---"
        self.assertEqual(
            MorseCodeConverter.morse_to_string(morse),
            "HELLO"
        )


if __name__ == '__main__':
    unittest.main()
