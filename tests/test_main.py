"""This module tests the main file"""

import typer
from typer.testing import CliRunner

import main

app = typer.Typer()
app.command()(main)

runner = CliRunner()


def test_app():
    result = runner.invoke(app, [ "main"])
    assert result.exit_code == 0
    assert "configator-generated" in result.stdout
    assert "true" in result.stdout
    assert "false" in result.stdout
    assert "2" in result.stdout
    assert "v1.1.0" in result.stdout
    assert "0.5.1" in result.stdout
    assert "3" in result.stdout