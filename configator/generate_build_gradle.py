
""""Function to generate a gradlebuild file"""

print("Let's work on getting your build.gradle file generated!")

def create_gradlebuild():
    """
    creating a file with gatorgradle version
    that can be read and written to
    """

#creating a variable and assigning it to strings for desired output
    gradlebuild = """
plugins {
    id "org.gatored.gatorgradle" version "0.5.1"
}
"""
#creating a build.gradle file
    with open("build.gradle", "w", encoding="utf8") as generate:
        #using write function with the variable gradlebuild
        generate.write(gradlebuild)
        #closing the file after writing
        generate.close()
