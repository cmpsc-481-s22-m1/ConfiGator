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
---

# A check inside these blocks runs on the "." directory against the "build.gradle" file
config:
gatorgrader.yml:
    --description "Make a gatorgrader.yml file" ConfirmFileExists

# A check without a surrounding block runs in the "." directory
--description "Have at least 7 commits" CountCommits --count 7

# A pure check runs directly as a shell command
(pure) test 2 -eq 2
"""
    with open("config/gatorgrader.yml", "w", encoding="utf8") as generate:
        generate.write(gatorgrader_config)
        generate.close()

    print("Let's work on getting your configuration files generated!")
# print("All the necessary configuration files have been created
# and placed into the '% s'" % directory)

#if __name__ == '__main__':
#    pass
