"""Creates pa file that will allow GatorGradle to run through GitHub Actions"""
import os

def create_configator_file(file):
    """Creating a file that will allow GatorGradle to run through GitHub Actions"""
    directory = ".github/workflows"
    if not os.path.exists(directory):
        os.makedirs(directory)

    data = """name: Grade
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

    with open(file, 'w', encoding='utf-8') as create_file:
        create_file.write(data)

if __name__ == "__main__":
    create_configator_file('../.github/workflows/grade.yml')
