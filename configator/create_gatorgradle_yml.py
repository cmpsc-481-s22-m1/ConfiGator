""""Program to automatically generate gatorgrader.yml files in a config directory"""

# import necessary libraries
import os

#pylint: disable=too-many-arguments
def create_gatorgrader(name, brk, fastfail, indent, version):
    """creating directory that can have files
    that can be read and written to.
    """
    # creating directory called config
    directory = "config"

    if os.path.isdir(directory) is True:
        pass
    else:
        os.mkdir(directory)

    gatorgrader_config = f"""
---
# The name of your assignment
name: {name}
# Should a check failure "break" the Gradle run?
break: {brk}
# Should a check failure immediately "break" the Gradle run?
fastfail: {fastfail}
# What level of indentation does the body of this file use?
indent: {indent}
# What version of GatorGrader should this assignment use?
version: {version}
---
"""
    with open("config/gatorgrader.yml", "w", encoding="utf8") as generate:
        generate.write(gatorgrader_config)
        generate.close()
