"""This module tests the githubactions module"""

from configator import create_actions_config


def test_create_configator_file_creates_github_actions(mocker):
    """ Testing to see if a file is created through github_actions"""
    mock_open = mocker.mock_open()
    #take in buildin open function and replace with mock function
      mocker.patch('builtins.open', mock_open)
      mocker.patch("os.makedirs")
      create_actions_config.create_configator_file()
      mock_open.assert_called_once_with(".github/workflows/grade.yml","w", encoding='utf-8')
