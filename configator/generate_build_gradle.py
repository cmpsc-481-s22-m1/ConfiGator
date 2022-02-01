
""""Function to generate a gradlebuild file"""

# import typer
#
# def cli(
#     Gradlebuild: bool = typer.Option(False)
# ):
#     print(f"Gradlebuild: {Gradlebuild}")
#
#     """
#     creating a file with gatorgradle version
#     that can be read and written to
#     """
#
#     gradlebuild = """
# plugins {
#     id "org.gatored.gatorgradle" version "0.5.1"
# }
# """
# #creating a build.gradle file
#     with open("build.gradle", "w", encoding="utf8") as generate:
#         #using write function with the variable gradlebuild
#         generate.write(gradlebuild)
#
#     print("Let's work on getting your build.gradle file generated!")
#
# if __name__ == '__main__':
#     cli()

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

    print("Let's work on getting your build.gradle file generated!")
