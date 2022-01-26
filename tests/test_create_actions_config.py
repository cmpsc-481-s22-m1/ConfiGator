"""This module tests the hello.say_hello module."""

import pytest


"""
@pytest.mark.parametrize(
    "name,expected",
    [
        ("World", "Hello, World!\n"),
        ("Maria", "Hello, Maria!\n"),
        ("Saejin", "Hello, Saejin!\n"),
    ],
)
def test_greet(capsys, name, expected):
    say_hello.greet(name)
    captured = capsys.readouterr()
    assert captured.out == expected

"""
