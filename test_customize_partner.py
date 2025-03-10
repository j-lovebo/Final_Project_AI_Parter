from unittest.mock import patch
from Customize_Partner import customize_partner  # Ensure the import path is correct

# Test 1: Regular partner details
def test_customize_partner_1():
    with patch('builtins.input', side_effect=["Alex", "25", "Male", "tall and strong", "friendly and outgoing"]):
        customize_partner()  # Expected output: Prints the customized partner's details

# Test 2: Short responses
def test_customize_partner_2():
    with patch('builtins.input', side_effect=["Jo", "30", "Female", "short", "calm"]):
        customize_partner()  # Expected output: Prints the customized partner's details

# Test 3: Unusual values
def test_customize_partner_3():
    with patch('builtins.input', side_effect=["X", "100", "Other", "glowing blue", "mysterious"]):
        customize_partner()  # Expected output: Prints the customized partner's details

# Test 4: Special characters in responses
def test_customize_partner_4():
    with patch('builtins.input', side_effect=["Zara!", "22", "Non-binary", "✨sparkly✨", "hyper & chaotic!"]):
        customize_partner()  # Expected output: Prints the customized partner's details

# Running the tests
test_customize_partner_1()
test_customize_partner_2()
test_customize_partner_3()
test_customize_partner_4()
