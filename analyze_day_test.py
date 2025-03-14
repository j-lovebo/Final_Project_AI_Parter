import unittest
from Analyze_Day import analyze_day

class TestAnalyzeDay(unittest.TestCase):

    def test_happy_response(self):
        result = analyze_day("I had a fantastic and joyful day!")
        self.assertEqual(result.strip(), "I'm glad to hear that! You deserve a good day every day!")

    def test_sad_response(self):
        result = analyze_day("It was a terrible and lonely day.")
        self.assertEqual(result.strip(), "I'm sorry to hear that. It's okay to feel down sometimes, but remember that everyone has tough days. Try to do something that makes you happy!")

    def test_angry_response(self):
        result = analyze_day("I am so annoyed and frustrated!")
        self.assertEqual(result.strip(), "That sounds frustrating. Try taking some deep breaths to calm yourself down. :)")

    def test_neutral_response(self):
        result = analyze_day("I'm okay, just a normal day.")
        self.assertEqual(result.strip(), "Nothing wrong with a chill day! :)")


    def test_mixed_emotions_response(self):
        result = analyze_day("It was an amazing but difficult day.")
        self.assertTrue("Hopefully it will get better!" in result)

if __name__ == '__main__':
    unittest.main()
