"""This module tests the main file"""

import typer
from typer.testing import CliRunner

import main

app = typer.Typer()
app.command()(main)

runner = CliRunner()


def test_app(mocker):
    result = runner.invoke(app, [ "main"])
    assert result.exit_code == 0
    mock_open = mocker.mock_open()
    #take in buildin open function and replace with mock function
    mocker.patch('builtins.open', mock_open)
    main.main()
    assert "configator-generated" in mock_open().write.call_args.args[0]
    assert "true" in mock_open().write.call_args.args[0]
    assert "false" in mock_open().write.call_args.args[0]
    assert "2" in mock_open().write.call_args.args[0]
    assert "v1.1.0" in mock_open().write.call_args.args[0]
    assert "0.5.1" in mock_open().write.call_args.args[0]
    assert "3" in mock_open().write.call_args.args[0]