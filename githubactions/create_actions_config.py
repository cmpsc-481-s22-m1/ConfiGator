from ruamel import yaml

def create_ConfiGator_file(target_file)
  "Creating a file that will allow GatorGradle to run through GitHub Actions"
  name: Grade
on: [push, pull_request]

jobs:
  grade:
    runs-on: ubuntu-latest
    name: Grade
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
        with:
          fetch-depth: 0
      - name: Run GatorGradle
        uses: GatorEducator/gatorgradle-action@v1
          
