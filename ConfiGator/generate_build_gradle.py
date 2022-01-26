
""""Function to generate a gradlebuild file"""

# import necessary libraries
import os

print("Let's work on getting your build.gradle file generated!")

def create_gradlebuild():
    """
    creating a file with gatorgradle version
    that can be read and written to
    """

    gradlebuild = """
plugins {
    id "org.gatored.gatorgradle" version "0.5.1"
}
"""
    f = open("build.gradle", "w")
    f.write(gradlebuild)
    f.close()
