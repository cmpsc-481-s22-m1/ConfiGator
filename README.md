# ConfiGator

![Mr.ConfiGator himself](img/icon.png)

[![Lint and Test](https://github.com/cmpsc-481-s22-m1/ConfiGator/actions/workflows/main.yml/badge.svg?branch=release%2F0.1.0)](https://github.com/cmpsc-481-s22-m1/ConfiGator/actions/workflows/main.yml)

A configuration file generator meant to be used with [GatorGradle](https://github.com/GatorEducator/gatorgradle).

## Overview

ConfiGator is a tool to be used in hand with GatorGradle to generate configuration
files for assignments that require GatorGradle. ConfiGator uses
[Poetry](https://python-poetry.org/) for package and dependency management.

## Usage

### Installing ConfiGator

Command to install ConfiGator

```bash
pipx install configator
```

### Commands to Change Specific Information Within a File

Command to change name

```bash
 configator --name {your name}
```

Command to change break format

```bash
configator --brk {false}
```

Command to change fast fail

```bash
configator --ff {true}
```

Command to change indentation

```bash
configator --ind {desired int}
```

Command to change GatorGrader version

```bash
configator --vers {desired version}
```

Command to change GatorGradle

```bash
configator --ggradleversion {desired version}
```

Command to change commit requirements

```bash
configator --com {desired int}
```

### Testing Program

Command to test the coverage

```bash
poetry run task test
```

### If you need Assistance 

Create an issue or a discussion post for assistance if you 
encounter any issues with ConfiGator.

### Contributors 

- [@connellyw](https://github.com/connellyw)
- [@donizk](https://github.com/donizk)
- [@Kevin487](https://github.com/Kevin487)
- [@Peter-Snipes]https://github.com/Peter-Snipes
- [@kailaniwoodard](https://github.com/kailaniwoodard)
- [@mariakimheinert](https://github.com/mariakimheinert)
- [@Michionlion](https://github.com/Michionlion)
