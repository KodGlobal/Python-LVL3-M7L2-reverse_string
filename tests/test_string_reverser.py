# test_string_reverser.py

import pytest
from reverse_string.string_reverser import reverse_string

# Testing the reverse_string function with a normal string.
def test_reverse_string_normal():
    assert reverse_string("hello") == "olleh", "Expected the string 'hello' to be reversed to 'olleh'"

# Checking the correctness of the reverse_string function when the string contains spaces.
def test_reverse_string_with_spaces():
    assert reverse_string("hello world") == "dlrow olleh", "Expected the string 'hello world' to be reversed to 'dlrow olleh'"

# It's important to ensure that the reverse_string function correctly handles an empty string without causing errors.
def test_reverse_string_empty():
    assert reverse_string("") == "", "Expected an empty string to be reversed to an empty string"