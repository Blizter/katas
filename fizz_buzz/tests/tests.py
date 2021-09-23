import pytest

from app.main import fizz_buzz

class TestFizzBuzz:
    def test_not_multiple(self):
        assert fizz_buzz(num=2) == 2
    def test_multiple_of_three(self):
        assert fizz_buzz(num=3) == "Fizz"
    def test_multiple_of_five(self):
        assert fizz_buzz(num=5) == "Buzz"
    def test_multiple_of_three_and_five(self):
        assert fizz_buzz(num=15) == "FizzBuzz"
