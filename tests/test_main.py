"""This module tests the main file"""

import typer
from typer.testing import CliRunner
from main import main

app = typer.Typer()
app.command()(main)

runner = CliRunner()


def test_app(mocker):
    """This module tests the main file for expected values being generated"""
    mock_open = mocker.mock_open()
    result = runner.invoke(app, ["--name", "test"])
    mock_open.assert_called_once_with("../test", "w", encoding="utf8")
    assert result.exit_code == 0
