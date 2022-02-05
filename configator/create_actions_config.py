"""Creates pa file that will allow GatorGradle to run through GitHub Actions"""
import os

def create_configator_file():
    """Creating a file that will allow GatorGradle to run through GitHub Actions"""
    direct = ".github/workflows"

    # if directory already exists, don't create directory
    if os.path.isdir(direct) is True:
        pass
    else:
      # create directories
        os.makedirs(direct)

    data = """
name: Grade
on: [push, pull_request]
jobs:
grade:
  runs-on: ubuntu-latest
  steps:
    - name: Checkout repository
      uses: actions/checkout@v2
    - name: Run GatorGradle
      uses: GatorEducator/gatorgradle-action@v1
"""
    file = ".github/workflows/grade.yml"

    with open(file, 'w', encoding='utf-8') as create_file:
        create_file.write(data)
