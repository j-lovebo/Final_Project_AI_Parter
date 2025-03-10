import unittest
from Customize_Partner import customize_partner  # Assuming the Partner class is imported


class TestCustomizePartner(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(customize_partner("John", 25, "Male", "tall", "kind"),
                         "Hello! I am your partner named John, who is 25 years old, looks tall, and has a kind personality!")

    def test_zero_age(self):
        self.assertEqual(customize_partner("John", 0, "Male", "tall", "kind"),
                         "Hello! I am your partner named John, who is 0 years old, looks tall, and has a kind personality!")

    def test_empty_name(self):
        self.assertEqual(customize_partner("", 25, "Male", "tall", "kind"),
                         "Hello! I am your partner named , who is 25 years old, looks tall, and has a kind personality!")

    def test_negative_age(self):
        self.assertEqual(customize_partner("John", -5, "Male", "tall", "kind"),
                         "Hello! I am your partner named John, who is -5 years old, looks tall, and has a kind personality!")

    def test_empty_appearance(self):
        self.assertEqual(customize_partner("John", 25, "Male", "", "kind"),
                         "Hello! I am your partner named John, who is 25 years old, looks , and has a kind personality!")

    def test_empty_personality(self):
        self.assertEqual(customize_partner("John", 25, "Male", "tall", ""),
                         "Hello! I am your partner named John, who is 25 years old, looks tall, and has a  personality!")

    def test_output_format(self):
        output = customize_partner("John", 25, "Male", "tall", "kind")
        self.assertTrue(output.startswith("Hello! I am your partner named"))
        self.assertTrue(output.endswith("personality!"))


if __name__ == '__main__':
    unittest.main()
