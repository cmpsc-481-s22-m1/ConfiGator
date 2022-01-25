"""This module tests the ConfiGator module."""

import pytest
import os

from src import ConfiGator

""" tests create_gatorgrader function, specifically 
the creation of the config file
"""

def test_create_gatorgrader_makes_config_directory(mocker):
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('os.mkdir')
    ConfiGator.create_gatorgrader()
    os.mkdir.assert_called_once_with('config')

""" tests create_gatorgrader function, specifically 
gatorgrader.yml containing fastfail condition
"""

def test_create_gatorgrader_writes_fastfail(mocker):
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('os.mkdir')
    ConfiGator.create_gatorgrader()
    assert "fastfail: false" in mock_open().write.call_args.args[0]

""" tests create_gatorgrader function, specifically open and 
write into a file called gatorgrader.yml in a directory called config
"""

# def test_create_gatorgrader_opens_and_writes_to_file(mocker):
#     mock_open = mocker.mock_open()
#     mocker.patch('builtins.open', mock_open)
#     mocker.patch('os.mkdir')
#     ConfiGator.create_gatorgrader()
#     assert in mock_open()

# check open is called with path
# was the file created w the str break:true

# write tests for open and in write mode and then 
# test if contents contain break:true
# call_args --> what the arguments are, assert what call_args contains