"""This module tests the main file"""

import typer
from typer.testing import CliRunner
from main import main

app = typer.Typer()
#app.command()(main)

runner = CliRunner()


def test_app(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    result = runner.invoke(app, ["--name", "test"])
    assert "name: test" in mock_open().write.call_args.args[0]
    assert result.exit_code == 0
