import os

script_dir = os.path.dirname(os.path.abspath(__file__))  # Path to this file directory

ls_dir = next(os.walk(script_dir))
last_dir_name = os.path.basename(
    os.path.normpath(script_dir)
)  # Name of this file directory
dirs = ls_dir[1]  # List all folders in this file directory
files = ls_dir[2]  # List all files in this file directory
with open(script_dir + "/README.md", "a+") as f:
    f.write(f"\n# {last_dir_name}\n")
    f.write("\nThis folder contains TODO\n")
    f.write("\n## Structure\n")
    f.write("\n### Folders\n")
    for dir_ in dirs:
        f.write(f"- `{dir_}` : TODO\n\n")

    f.write("### Files\n")
    for file_ in files:
        if file_ != "output-structure-for-readme.py":
            f.write(f"- `{file_}` : TODO\n\n")
