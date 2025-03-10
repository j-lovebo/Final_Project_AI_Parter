from unittest.mock import patch
from Name_Response import name_response  # Ensure the import path is correct

# Test 1: Regular name
def test_name_response_1():
    with patch('builtins.input', return_value="Alice"):
        name_response("Alice")  # Expected output: "Wow, Alice is such a beautiful name!"

# Test 2: A name with special characters
def test_name_response_2():
    with patch('builtins.input', return_value="J@ne_Doe"):
        name_response("J@ne_Doe")  # Expected output: "Wow, J@ne_Doe is such a beautiful name!"

# Running the tests
test_name_response_1()
test_name_response_2()
