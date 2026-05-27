"""Test suite for fibonacci.py — Lab 1: Software Construction.

Do NOT modify this file. Your implementation in fibonacci.py must
pass every test below before you open your Pull Request.

Run with:
    pytest test_fibonacci.py -v
"""

import pytest

from fibonacci import fibonacci


class TestFibonacciBaseCase:
    """Tests for base cases of the Fibonacci sequence."""

    def test_fibonacci_zero(self):
        assert fibonacci(0) == 0

    def test_fibonacci_one(self):
        assert fibonacci(1) == 1


class TestFibonacciSequence:
    """Tests for correct sequence values."""

    def test_fibonacci_two(self):
        assert fibonacci(2) == 1

    def test_fibonacci_three(self):
        assert fibonacci(3) == 2

    def test_fibonacci_ten(self):
        assert fibonacci(10) == 55

    def test_fibonacci_fifteen(self):
        assert fibonacci(15) == 610

    def test_fibonacci_twenty(self):
        assert fibonacci(20) == 6765

    @pytest.mark.parametrize("n, expected", [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
    ])
    def test_fibonacci_sequence_parametrized(self, n, expected):
        assert fibonacci(n) == expected


class TestFibonacciEdgeCases:
    """Tests for error handling and edge cases."""

    def test_negative_input_raises_value_error(self):
        with pytest.raises(ValueError):
            fibonacci(-1)

    def test_large_negative_raises_value_error(self):
        with pytest.raises(ValueError):
            fibonacci(-100)

    def test_float_input_raises_type_error(self):
        with pytest.raises(TypeError):
            fibonacci(3.5)

    def test_string_input_raises_type_error(self):
        with pytest.raises(TypeError):
            fibonacci("five")

    def test_none_input_raises_type_error(self):
        with pytest.raises(TypeError):
            fibonacci(None)


class TestFibonacciReturnType:
    """Tests that the return type is always an integer."""

    def test_returns_integer_for_zero(self):
        assert isinstance(fibonacci(0), int)

    def test_returns_integer_for_positive(self):
        assert isinstance(fibonacci(7), int)
