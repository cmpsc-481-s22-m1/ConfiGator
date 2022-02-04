"""Element of the Configator tool to enable default README.md generation"""

print("Generating default README...!")

def create_readme():
    """ method to generate README
    """
    with open("../README.md", "w", encoding="utf8") as read_me:
        read_me.write("This is text.")

create_readme()
