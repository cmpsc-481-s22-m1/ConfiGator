"""Element of the Configator tool to enable default README.md generation"""

print("Generating default README...!")

# method to generate README
def create_readme():
    f = open("../README.md", "w")
    f.write("This is text.")
    f.close()

create_readme()