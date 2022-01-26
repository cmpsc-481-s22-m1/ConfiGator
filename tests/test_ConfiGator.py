"""This module tests the ConfiGator module."""

import pytest

from configator import generate_build_gradle

def test_create_gatorbuild_generates_file_named_build_gradle(mocker):
    mock_open = mocker.mock_open()
    #take in buildin open function and replace with mock function
    mocker.patch('builtins.open', mock_open)
    generate_build_gradle.create_gradlebuild()
    mock_open.assert_called_once_with("build.gradle","w")

def test_create_gradlebuild_writes_through_gradlebuild(mocker):
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    generate_build_gradle.create_gradlebuild()
    assert "gatorgradle" in mock_open().write.call_args.args[0]
