# You have 2 types of modules, builtins or external. Built ins come pre-installed with Python.
# For 3rd party modules you needs to locate them - Python docs for example.
# PIP is a package manager. It allows you to install and manage external packages into Python.
# Open Terminal on Mac and check that PIP is installed. Should be pre-installed.
# pi  --version will show you the version installed.
# pip install python-docx will install python docx.
import tool_to_import

print(tool_to_import.get_file_extension("word.pdf"))
print(tool_to_import.dice_roll(50))

