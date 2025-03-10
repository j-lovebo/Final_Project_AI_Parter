from unittest.mock import patch
from Worry_Question import ask_worry  # Make sure the import path is correct

# Test 1: User says "yes" to worry, "yes" to talk, shares feelings, and gives a destress activity
def test_worry_1():
    with patch('builtins.input', side_effect=["yes", "yes", "I'm feeling anxious", "Taking walks"]):
        ask_worry()

# Test 2: User says "yes" to worry, "no" to talk, and gives a destress activity
def test_worry_2():
    with patch('builtins.input', side_effect=["yes", "no", "Taking a walk"]):
        ask_worry()

# Test 3: User says "no" to worry and gives a destress activity
def test_worry_3():
    with patch('builtins.input', side_effect=["no", "Taking a walk"]):
        ask_worry()

# Test 4: User provides invalid input (neither yes nor no) for worry
def test_worry_4():
    with patch('builtins.input', side_effect=["maybe", "Taking a walk"]):
        ask_worry()

# Running the tests shows each of the 4 ways it could go
test_worry_1()
test_worry_2()
test_worry_3()
test_worry_4()
