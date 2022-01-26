"""Creates pa file that will allow GatorGradle to run through GitHub Actions"""
from ruamel import yaml

def create_configator_file(config_file):
    """Creating a file that will allow GatorGradle to run through GitHub Actions"""
    data = """\
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
    file = yaml.round_trip_load(data)

    with open(config_file, 'w', encoding='utf-8') as create_file:
        yaml.round_trip_dump(file, create_file, indent=2)

if __name__ == "__main__":
    create_configator_file('../.github/workflows/grade.yml')
