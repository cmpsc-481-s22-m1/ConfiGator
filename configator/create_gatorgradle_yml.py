""""Program to automatically generate gatorgrader.yml files in a config directory"""

# import necessary libraries
import os

import main

def create_gatorgrader(name, brk, ff, ind, vers, com):
    """creating directory that can have files
    that can be read and written to.
    """
    # creating directory called config
    directory = "config"

    os.mkdir(directory)
    # if directory exists, error
    gatorgrader_config = f"""
---
# The name of your assignment
name: {name}
# Should a check failure "break" the Gradle run?
break: {brk}
# Should a check failure immediately "break" the Gradle run?
fastfail: {ff}
# What level of indentation does the body of this file use?
indent: {ind}
# What version of GatorGrader should this assignment use?
version: {vers}
# Minimum commit requirement?
commits: {com}
---
"""
    with open("C:/kyrie/config/gatorgrader.yml", "w", encoding="utf8") as generate:
        generate.write(gatorgrader_config)
        generate.close()

#if __name__ == '__main__':
#    pass
