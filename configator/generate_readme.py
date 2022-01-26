# """Element of the Configator tool to enable default README.md generation"""

# # Import necessary packages
# from os.path import exists as file_exists

# def if_exists():
#     if file_exists('../README.md'):
#         return True
#     return False

# # Import contents of default README_template.md
# base_file = open('public/static/README_template.md', 'r')

# # Save contents of the base file to a String
# file_content = base_file.read()

# # Instantiate read_me variable as a file
# read_me = open('../README.md', 'r')

# # Import the file contents to the actual README.md file
# while if_exists():
#     read_me.write(file_content)

import os

print("Let's generate your readme!")

# method to generate README
def create_readme():
    f = open("Desktop/README.md", "w")
    f.write("This is text.")
    f.close()