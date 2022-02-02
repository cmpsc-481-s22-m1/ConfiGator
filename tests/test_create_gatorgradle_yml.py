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
