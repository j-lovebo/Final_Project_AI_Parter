import random
from unittest.mock import patch
from Random_Questions import ask_random_question

# Test 1: Run the random question function and see if it works without errors
def test_ask_random_question():
    print("\nTest 1: Running ask_random_question() without mocks:")
    ask_random_question()  # Run the function to see if it works

# Test 2: Run the random question function with a mocked input to see if it doesn't fail
def test_ask_random_question_with_mocked_input():
    print("\nTest 2: Running ask_random_question() with mocked input:")
    # Mocking user input to avoid interactive prompts
    with patch('builtins.input', return_value="Test response"):
        ask_random_question()

# Run the tests
test_ask_random_question()
test_ask_random_question_with_mocked_input()
