"""This module tests the main file"""

from typer.testing import CliRunner
from main import app

runner = CliRunner()


def test_name_option_updates_assignmentname(mocker):
    """This module tests if the name of the assignement is able to be changed"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--name", "test"])
    assert "name: test" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_break_option_updates_false(mocker):
    """This module tests if the break is able to be changed"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--brk", "false"])
    assert "break: false" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_ffail_option_updates_true(mocker):
    """This module tests if fast fail is able to be enabled"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--fastfail", "true"])
    assert "fastfail: true" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_indent_option_updates_indentation(mocker):
    """This module tests if the indentation is able to be changed"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--ind", "1"])
    assert "indent: 1" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_vers_option_updates_version(mocker):
    """This module tests if the version is able to be updated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--vers", "v2.1.0"])
    assert "version: v2.1.0" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_ggradleversion_option_changes_version(mocker):
    """This module tests if the gator gradle version is able to be changed"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--ggradleversion", "0.6.0"])
    assert "0.6.0" in mock_open().write.call_args_list[1].args[0]
    assert result.exit_code == 0

def test_com_option_updates_commits(mocker):
    """This module tests if the commits number is able to be changed"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--com", "4"])
    assert "commits: 4" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0
