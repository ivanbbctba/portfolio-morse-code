import unittest
from morse_code_converter.morse_code import MorseCodeConverter
from parameterized import parameterized


class TestMorseCodeConverter(unittest.TestCase):

    @parameterized.expand([
        ("simple_text", "hello", ".... . .-.. .-.. ---"),
        ("capitalization", "Hello", ".... . .-.. .-.. ---"),
        ("numbers_and_punctuation", "123?", ".---- ..--- ...-- ..--.."),
        ("spaces_between_words", "HELLO WORLD", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
        ("unrecognized_characters", "@#$", "??? ??? ???")
    ])
    def test_string_to_morse(self, name, input_string, expected_output):
        self.assertEqual(MorseCodeConverter.string_to_morse(input_string), expected_output)

    @parameterized.expand([
        ("simple_text", ".... . .-.. .-.. ---", "HELLO"),
        ("numbers", ".---- ..--- ...--", "123"),
        ("complex_example", "... --- ... / .... . .-.. .--.", "SOS HELP")
    ])
    def test_reverse_conversion(self, name, input_string, expected_output):
        self.assertEqual(MorseCodeConverter.morse_to_string(input_string), expected_output)


if __name__ == '__main__':
    unittest.main()
