# You can open files with the open() function. You can specify the relative path if its in the same directory
# or the absolute path if its in another directory. You can specify the mode as the second key-word argument
# Use the close function on the variable with the file open in it to close the file.
# "r" = read only  "w" = write  "a" = append  "r+" = Read and Write

# file = open("employees.txt", "r+")

# print(file.readable())      #Check to see if Python can actually see the file contents.
# print(file.read())        # This shows the entire contents of the file
# print(file.readline())    # Reads first line, subsequent readline() functions iterate through lines in file.
# print(file.readlines()[2])     # Saves each line to a list. Indexes can then reference lines. Index outside function.

# In the example below you have to put the readline function in the for expression at the top. If you say for line in
# file: then the file doesn't have a list to iterate through. But file.readlines() converts it into the list for the for
# loop to then iterate through.

# for line in file.readlines():
    # print(line)

# file.close()

# ---------------------------------- Writing to Files ------------------------------------------------------------
# With the a argument the new employees were appended to th end of the document. With w all the others were deleted
# and only 1 added. If you specify a file name hat doesn't exist, Python will create it.

file = open("employeesNEW.txt", "w")
file.write("\nDaisy & Ivy - Emotional Support")     # Remember the escape characters!
