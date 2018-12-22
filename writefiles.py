# Write files
# mode - Write (w) clear the files and starts writing from beginning
# mode - ammend (a) append to end of the file


with open('Files/write.txt','w') as myFile:
    myFile.write('Hello')


with open('Files/write.txt','a') as myFile:
    myFile.write('\n How are you doing?')



    lines = ['\n How are you doing Hari?',
            '\n Iam doing great',
            '\n Thanks']

with open('Files/write.txt','a') as myFile:
    myFile.writelines(lines)