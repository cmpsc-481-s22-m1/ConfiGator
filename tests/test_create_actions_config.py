"""This module tests the githubactions module"""
    
import pytest

from configator import create_actions_config

def test_create_configator_file_creates_github_actions(mocker):
    mock_open = mocker.mock_open()
    #take in buildin open function and replace with mock function
    mocker.patch('builtins.open', mock_open)
    configator_file.create_gradlebuild()
    mock_open.assert_called_once_with("build.gradle","w")
    
def test_create_create_configator_file_has_text_inside(mocker):
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    create_actions_config.create_gradlebuild()
    mock_open.assert_called_once_with("build.gradle","w")


#write unit testing, which is expected in this project. invoke each part of the program
# invoke create_configator Function
#open function and write function was used to generate this file
#with right parameters it should pass test by generating correct file through open
#did you pass the right parameter? (check it)
#did you pass build.gradle in open function? (confident build.gradle was created)
#write function, if gradle build (the right string) was passed into the function
