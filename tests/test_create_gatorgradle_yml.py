"""This program will test the create gatorgradle yml file"""

#import os

from configator import create_gatorgradle_yml


def test_create_gatorgrader_writes_fastfail(mocker):
    """tests create_gatorgrader function, specifically
    gatorgrader.yml containing fastfail condition.
    """
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    mocker.patch('os.mkdir')
    create_gatorgradle_yml.create_gatorgrader("configator-generated",
    "true", "false", 2, "v1.1.0", 3)
    assert "fastfail: false" in mock_open().write.call_args.args[0]
