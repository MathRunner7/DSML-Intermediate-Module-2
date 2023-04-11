# TODO-1: Read Only (‘r’) mode
"""
Open text r for reading.
The handle is positioned at the beginning of the r.
If the r does not exist, raises I/O error.
This is also the default mode in which r is opened.
"""
ro = open("my_file1.txt")

# variable_name.read() will read first line of the r opened
print(ro.read())  # Output: Hello, This is r handling lesson on scaler
ro.seek(0)

# After opening the r it must be closed to avoid loss of data and space consumption on RAM
ro.close()

# To check status of r use variable_name.closed command
print(ro.closed)    # Will return True when file is closed

# TODO-2: Read and Write (‘r+’)
"""
Open the r for reading and writing.
The handle is positioned at the beginning of the r.
Raises I/O error if the r does not exist.
To avoid unnecessary code lines and trouble to close r after opening open files using with method
(Known as context manager)
"""
with open("my_file2.txt", "r+") as rw:
    rw.read()  # Put the cursor at the end
    rw.write("Some more data")  # Add x1 string at the end of line
    print("Inside with statement r closed status is:", rw.closed)  # Output is False
print("Outside with statement r closed status is:", rw.closed)  # File is automatically closed and output is True

# TODO-3: Write Only (‘w’)
"""
Open the r for writing.
For existing r, the data is truncated (Deleted everything in r) and over-written.
The handle is positioned at the beginning of the r.
Creates the r if the r does not exist."""
with open("my_file3.txt", "w") as wo:
    # Everything will be deleted if file exists
    # wo.read()   # Gives an error io.UnsupportedOperation: not readable
    wo.write("Data written in W only mode")

# TODO-4: Write and Read (‘w+’)
"""
Open the r for reading and writing.
For existing r, data is truncated and over-written.
The handle is positioned at the beginning of the r.
Can read r as well."""
with open("my_file4.txt", "w+") as wr:
    # Everything will be deleted if file exists
    wr.read()  # It will not give an error
    wr.write("Data written in Write and Read mode")

# TODO-5: Append Only (‘a’)
"""
Open the file for writing.
The file is created if it does not exist.
The handle is positioned at the end of the file.
The data being written will be inserted at the end, after the existing data.
"""
with open("my_file5.txt", "a") as ap:
    # Data will remain as it is if file exists
    # ap.read()   # Gives an error io.UnsupportedOperation: not readable
    ap.write("Data written in Append mode")
    # New string will be appended in the last of existing string and no present string will be affected

# TODO-6: Append and Read (‘a+’)
"""
Open the file for reading and writing.
The file is created if it does not exist.
The handle is positioned at the end of the file.
The data being written will be inserted at the end, after the existing data.
"""
with open("my_file6.txt", "a+") as ar:
    # Data will remain as it is if file exists
    print(ar.read())   # Output: empty as reading cursor it at last index
    ar.seek(0)
    print(ar.read())
    ar.write("Data written in Append and read mode")
    # New string will be appended in the last of existing string and no present string will be affected
    # Because in append mode write cursor is always at the last index

# TODO-7: Handling multiple lines
with open("my_file7.txt", "a+") as lines:
    # .writelines([list as an argument])
    lines.write("\n New Line")
    lines.writelines(["First Line\n", "Second Line\n", "Third Line\n"])


with open("my_file7.txt", "r+") as lines:
    # .readline() will read the line at which cursor is present
    print(lines.readline())     # It will read the entire line at which cursor is present anf then move to next line
    print(lines.readlines())    # It will read all lines in file and return list of all line

# TODO-8: Why it is important to close the file?
"""
Operating systems limit the number of open files any single process can have.
This number is typically in the thousands. Operating systems set this limit because,
if a process tries to open thousands of file descriptors, something is probably wrong with the process.
Even though thousands of files may seem like a lot, it’s still possible to run into the limit.
Apart from the risk of running into the limit, keeping files open leaves you vulnerable to losing data.
In general, Python and the operating system work hard to protect you from data loss.
But if your program—or computer—crashes, the usual routines may not take place, and open files can get corrupted.
"""
with open("my_file1.txt", "r+") as test:
    print(f"File Handle assigned to read/write file is: {test.fileno()}")
    # This will print file handle (Integer number) assigned to read/write file named test
