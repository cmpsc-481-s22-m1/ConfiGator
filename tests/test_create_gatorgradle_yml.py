"""This module tests the configator module."""

import os

from configator import create_gatorgradle_yml


def test_create_gatorgrader_makes_config_directory(mocker):
    """tests create_gatorgrader function, specifically
    the creation of the config file.
    """
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('os.mkdir')
    create_gatorgradle_yml.create_gatorgrader()
    os.mkdir.assert_called_once_with('config')


def test_create_gatorgrader_writes_fastfail(mocker):
    """tests create_gatorgrader function, specifically
    gatorgrader.yml containing fastfail condition.
    """
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('os.mkdir')
    create_gatorgradle_yml.create_gatorgrader()
    assert "fastfail: false" in mock_open().write.call_args.args[0]


def test_create_gatorgrader_opens_and_writes_to_file(mocker):
    """tests create_gatorgrader function, specifically open and
    write into a file called gatorgrader.yml in a directory called config
    """
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('os.mkdir')
    create_gatorgradle_yml.create_gatorgrader()
    mock_open.assert_called_once_with("config/gatorgrader.yml","w", encoding='utf-8')
    assert "fastfail: false" in mock_open().write.call_args.args[0]
