""""Function to generate a gradlebuild file"""

def create_gradlebuild(ggradleversion):
    """
    creating a file with gatorgradle version
    that can be read and written to
    """

#creating a variable and assigning it to strings for desired output
    gradlebuild = f'''
plugins {{
    id "org.gatored.gatorgradle" version "{ggradleversion}"
}}
'''
#creating a build.gradle file
    with open("build.gradle", "w", encoding="utf8") as generate:
        #using write function with the variable gradlebuild
        generate.write(gradlebuild)
