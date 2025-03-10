import unittest
from Analyze_Day import analyze_day


class TestAnalyzeDay(unittest.TestCase):
    def test_happy_response(self):
        self.assertEqual(analyze_day("I had a fantastic and joyful day!"),
                         "I'm glad to hear that! You deserve a good day everyday!")

    def test_sad_response(self):
        self.assertEqual(analyze_day("It was a terrible and lonely day."),
                         "I'm sorry to hear that, it's okay to feel down sometimes, but just remember that everyone has tough days. Try to do something that you know makes you happy!")

    def test_angry_response(self):
        self.assertEqual(analyze_day("I am so annoyed and frustrated!"),
                         "That sounds frustrating, try to take some deep breathes to calm yourself down :)")

    def test_neutral_response(self):
        self.assertEqual(analyze_day("I'm okay, just a normal day."), "Nothing wrong with a chill day:)")

    def test_unrecognized_response(self):
        with self.assertRaises(ValueError):
            analyze_day("xyz abc unknown")

    def test_mixed_emotions_response(self):
        self.assertEqual(analyze_day("It was an amazing but difficult day."),
                         "It seems like your day was happy, and angry. Hopefully it will get better!")


if __name__ == '__main__':
    unittest.main()