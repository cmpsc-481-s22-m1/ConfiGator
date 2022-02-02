# ConfiGator

![Mr.ConfiGator himself](img/icon.png)

[![Lint and Test](https://github.com/cmpsc-481-s22-m1/ConfiGator/actions/workflows/main.yml/badge.svg?branch=release%2F0.1.0)](https://github.com/cmpsc-481-s22-m1/ConfiGator/actions/workflows/main.yml)

A configuration file generator meant to be used with [GatorGradle](https://github.com/GatorEducator/gatorgradle).

## Overview

ConfiGator is a tool to be used in hand with GatorGradle to generate configuration
files for assignments that require GatorGradle. ConfiGator uses
[Poetry](https://python-poetry.org/) for package and dependency management.

## Usage

### Installing Python Dependencies

In order to install the dependencies of this project, run this command in your
command line:

```bash
poetry install
```

```bash
poetry install typer
```

After installing the dependencies, navigate to the repository directory, and run
the following in your command line:

```bash
poetry run python main.py
```

### Commands to Change Specific Information Within a File:

Command to change name
```bash
poetry run python main.py --name {your name}
```

Command to change break format
```bash
poetry run python main.py --brk {false}
```

Command to change fast fail
```bash
poetry run python main.py --ff {true}
```

Command to change indentation
```bash
poetry run python main.py --ind {desired int}
```

Command to change GatorGrader version
```bash
poetry run python main.py --vers {desired version}
```

Command to change GatorGradle
```bash
poetry run python main.py --ggradleversion {desired version}
```

Command to change commit requirements
```bash
poetry run python main.py --com {desired int}
```

### Testing Program

Command to test the coverage
```bash
poetry run task test
```