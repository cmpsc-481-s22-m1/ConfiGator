"""Element of the Configator tool to enable default README.md generation"""

print("Generating default README...!")

# method to generate README
def create_readme():
    read_me = open("../README.md", "w")
    read_me.write("This is text.")
    read_me.close()

create_readme()
