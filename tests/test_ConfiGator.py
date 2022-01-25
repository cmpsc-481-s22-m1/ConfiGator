"""This module tests the ConfiGator module."""

import pytest
import os

from src import ConfiGator

def test_create_gatorgrader_makes_config_directory(mocker):
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('os.mkdir')
    ConfiGator.create_gatorgrader()
    os.mkdir.assert_called_once_with('config')

def test_create_gatorgrader_writes_fastfail(mocker):
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('os.mkdir')
    ConfiGator.create_gatorgrader()
    assert "fastfail: false" in mock_open().write.call_args.args[0]

# check open is called with path
# was the file created w the str break:true

# write tests for open and in write mode and then 
# test if contents contain break:true
# call_args --> what the arguments are, assert what call_args contains