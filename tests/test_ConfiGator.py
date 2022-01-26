"""This module tests the ConfiGator module."""

import pytest

from configator import generate_build_gradle

def test_create_gatorbuild_generates_file_named_build_gradle(mocker):
    mock_open = mocker.mock_open()
    #take in buildin open function and replace with mock function
    mocker.patch('builtins.open', mock_open)
    generate_build_gradle.create_gradlebuild()
    mock_open.assert_called_once_with("build.gradle","w")

def test_create_gatorgrader_writes_fastfail(mocker):
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    generate_build_gradle.create_gradlebuild()
    assert "gatorgradle" in mock_open().write.call_args.args[0]

#write unit testing, which is expected in this project. invoke each part of the program
# invoke create_gradlebuild Function
#open function and write function was used to generate this file
#with right parameters it should pass test by generating correct file through open
#did you pass the right parameter? (check it)
#did you pass build.gradle in open function? (confident build.gradle was created)
#write function, if gradle build (the right string) was passed into the function
