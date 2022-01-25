
""""Command-line interface to receive input to create configuration files"""

# import necessary libraries
import os

print("Let's work on getting your build.gradle file generated!")

"""
creating directory that can have files
that can be read and written to
"""
def create_gradlebuild():

    os.mkdir(directory)
    gradlebuild = """
    plugins {
       id "org.gatored.gatorgradle" version "0.5.1"
    }
    """
    f = open("build.gradle", "w")
    f.write(gradlebuild)
    f.close()

if __name__ == '__main__':
    pass
