""""Program to automatically generate gatorgrader.yml files in a config directory"""

# import necessary libraries
import os

def create_gatorgrader():
    """creating directory that can have files
    that can be read and written to.
    """
    # creating directory called config
    directory = "config"

    os.mkdir(directory)
    # if directory exists, error
    gatorgrader_config = """
---
# The name of your assignment
name: simple-assignment
# Should a check failure "break" the Gradle run?
break: true
# Should a check failure immediately "break" the Gradle run?
fastfail: false
# What level of indentation does the body of this file use?
indent: 2
# What version of GatorGrader should this assignment use?
version: v1.1.0
# Minimum commit requirement?
commits: 3
---
"""
    with open("config/gatorgrader.yml", "w", encoding="utf8") as generate:
        generate.write(gatorgrader_config)
        generate.close()

#if __name__ == '__main__':
#    pass
