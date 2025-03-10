import unittest
import sys
from Analyze_Day import analyze_day
class TestAnalyzeDay(unittest.TestCase):

    def setUp(self):
        # Capture the original print function
        self.old_stdout = sys.stdout
        sys.stdout = self

    def write(self, data):
        # Capture the printed data
        self.output = data

    def test_happy_response(self):
        analyze_day("I had a fantastic and joyful day!")
        self.assertEqual(self.output.strip(), "I'm glad to hear that! What made your day so great?")

    def test_sad_response(self):
        analyze_day("It was a terrible and lonely day.")
        self.assertEqual(self.output.strip(), "I'm sorry to hear that. Do you want to talk about it?")

    def test_angry_response(self):
        analyze_day("I am so annoyed and frustrated!")
        self.assertEqual(self.output.strip(), "That sounds frustrating. What happened?")

    def test_neutral_response(self):
        analyze_day("I'm okay, just a normal day.")
        self.assertEqual(self.output.strip(), "Got it. Anything interesting happen today?")

    def test_unrecognized_response(self):
        # Test for unrecognized words, expecting the exception message to be printed
        analyze_day("xyz abc unknown")
        self.assertEqual(self.output.strip(), "Oh, sorry! I didn't quite understand that. Can you try again?")

    def test_mixed_emotions_response(self):
        analyze_day("It was an amazing but difficult day.")
        self.assertEqual(self.output.strip(), "That sounds frustrating. What happened?")

    def tearDown(self):
        # Restore the original stdout
        sys.stdout = self.old_stdout

if __name__ == '__main__':
    unittest.main()
