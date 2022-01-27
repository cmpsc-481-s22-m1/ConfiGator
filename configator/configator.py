from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle

if __name__ == '__main__':
  create_actions_config.create_configator_file()
  create_gatorgradle_yml.create_gatorgrader()
  generate_build_gradle.create_gradlebuild()
