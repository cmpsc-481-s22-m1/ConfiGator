"""This module tests the configator module."""

from configator import generate_build_gradle

def test_create_gatorbuild_generates_file_named_build_gradle(mocker):
    """Testing if file is generated using the function."""
    mock_open = mocker.mock_open()
    #take in buildin open function and replace with mock function
    mocker.patch('builtins.open', mock_open)
    generate_build_gradle.create_gradlebuild()
    mock_open.assert_called_once_with("build.gradle","w", encoding="utf8")

def test_create_gradlebuild_writes_through_gradlebuild(mocker):
    """Testing if gatorbuild string is present in generated file."""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    generate_build_gradle.create_gradlebuild()
    assert "gatorgradle" in mock_open().write.call_args.args[0]
