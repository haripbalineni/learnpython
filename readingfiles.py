#Reading the files

# Method 1
# oFile = open('Files/data1.txt')  # open

# for line in oFile:
#     print(line.rstrip())

# oFile.seek(0) # to move the cursor to first posistion
# lines = oFile.readlines()
# print(lines)

# oFile.seek(20) # to move the cursor to first posistion
# lines = oFile.readlines(50)
# print(lines)



# oFile.close()                    # Close the file here 


# Method 2 ( No need to close file here)

def escapeLine(line):
    return 'done' not in line


with open('Files/data1.txt')  as myFile:
        lines = myFile.readlines()
        print(list(filter(escapeLine,lines)))

    