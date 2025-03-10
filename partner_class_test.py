import unittest
from Partner_Class import Partner

class TestPartner(unittest.TestCase):

    def test_partner_initialization(self):
        partner = Partner("John", 30, "Male", "Tall, Blond", "Kind")
        self.assertEqual(partner.name, "John")
        self.assertEqual(partner.age, 30)
        self.assertEqual(partner.gender, "Male")
        self.assertEqual(partner.appearance, "Tall, Blond")
        self.assertEqual(partner.personality, "Kind")

    def test_partner_repr(self):
        partner = Partner("Alice", 25, "Female", "Short, Brunette", "Outgoing")
        self.assertEqual(repr(partner), "Partner(name=Alice, age=25, gender=Female, appearance=Short, Brunette, personality=Outgoing)")

    def test_missing_name(self):
        with self.assertRaises(TypeError):
            Partner(age=25, gender="Female", appearance="Short, Brunette", personality="Outgoing")

    def test_invalid_age(self):
        with self.assertRaises(TypeError):
            Partner("Charlie", "Twenty", "Male", "Tall, Black", "Funny")

    def test_invalid_gender(self):
        partner = Partner("Eve", 28, "Female", "Medium height, Black", "Serious")
        self.assertEqual(partner.gender, "Female")
        partner_invalid = Partner("Eve", 28, "InvalidGender", "Medium height, Black", "Serious")
        self.assertEqual(partner_invalid.gender, "InvalidGender")


if __name__ == '__main__':
    unittest.main()
