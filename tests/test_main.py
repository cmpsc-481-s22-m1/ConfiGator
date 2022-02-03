"""This module tests the main file"""

import typer
from typer.testing import CliRunner
from main import app

#app = typer.Typer()
#app.command()(main)

runner = CliRunner()


def test_name_option_updates_assignmentname(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--name", "test"])
    assert "name: test" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_break_option_updates_false(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--brk", "false"])
    assert "break: false" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_ffail_option_updates_true(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--fastfail", "true"])
    assert "fastfail: true" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_indent_option_updates_indentation(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--ind", "1"])
    assert "indent: 1" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_name_option_updates_assignmentname(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--vers", "v2.1.0"])
    assert "version: v2.1.0" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0

def test_ggradleversion_option_changes_version(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--ggradleversion", "0.6.0"])
    assert "0.6.0" in mock_open().write.call_args_list[1].args[0]
    assert result.exit_code == 0

def test_name_option_updates_assignmentname(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--com", "4"])
    assert "commits: 4" in mock_open().write.call_args_list[0].args[0]
    assert result.exit_code == 0
