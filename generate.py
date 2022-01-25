""""Command-line interface to receive input to create configuration files"""

import typer
import os

print("Let's work on getting your configuration files generated!")

cli = typer.Typer()

# directory
directory = "config"

# Path
path = os.path.join(directory)

"""
creating directory that can have files
that can be read and written to
"""

os.mkdir(directory, mode = 0o666)
print("Directory '% s' is built!" % directory)

def cli(
    gatorgrader: bool = typer.Option(False)
):

    print(f"gatorgrader: {gatorgrader}")

    """"Generating the gatorgrader.yml file"""

    f = open("config/gatorgrader.yml", "w")
    f.write("--- \n")
    f.write("# The name of your assignment\n")
    f.write("""# Should a check failure "break" the Gradle run?\n""")
    f.write("break: true\n")
    f.write("""# Should a check failure immediately "break" the Gradle run?\n""")
    f.write("fastfail: false\n")
    f.write("# What level of indentation does the body of this file use?\n")
    f.write("indent: 2\n")
    f.write("# What version of GatorGrader should this assignment use?\n")
    f.write("version: v1.1.0\n")
    f.write("---\n")
    f.write("\n")
    f.write("""# A check inside these blocks runs on the "." directory against the "build.gradle" file\n """)
    f.write("config:\n")
    f.write("  gatorgrader.yml:\n")
    f.write("""    --description "Make a gatorgrader.yml file" ConfirmFileExists\n""")
    f.write("\n")
    f.write("""# A check without a surrounding block runs in the "." directory\n""")
    f.write("""--description "Have at least 7 commits" CountCommits --count 7\n""")
    f.write("# A pure check runs directly as a shell command\n")
    f.write("(pure) test 2 -eq 2\n")
    f.close()

if __name__ == '__main__':
    cli()

def cli(
    Gradlebuild: bool = typer.Option(False)
):
    print(f"Gradlebuild: {Gradlebuild}")

    """"Generating the gradle.build file"""

    f = open("gradle.build", "w")
    f.write("plugins { \n")
    f.write("""   id "org.gatored.gatorgradle" version "0.5.1" \n""")
    f.write("}")
    f.close()

if __name__ == '__main__':
    cli()

def cli(
    Main: bool = typer.Option(False)
):
    print(f"Main: {Main}")

    """"Generating the main.py file"""

    f = open(".github/workflows/main.py", "w")
    f.write("name: Grade")
    f.write("on: [push, pull_request]\n")
    f.write("\n")
    f.write("jobs:\n")
    f.write("  grade:\n")
    f.write("    runs-on: ubuntu-latest\n")
    f.write("    name: Grade\n")
    f.write("    steps:\n")
    f.write("      - name: Checkout repository\n")
    f.write("        uses: actions/checkout@v2\n")
    f.write("        with:\n")
    f.write("          fetch-depth: 0\n")
    f.write("      - name: Run GatorGradle\n")
    f.write("        uses: GatorEducator/gatorgradle-action@v1")
    f.close()

if __name__ == '__main__':
    cli()
