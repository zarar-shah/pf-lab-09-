def numLines(filename):
    'return the number of lines in file filename'
    infile = open(filename, 'r')    #open the file and read it
    lineList = infile.readlines()   #into a list of lines
    infile.close()

    print(lineList)                  #print list of lines
    return len(lineList)

x = input("Enter file: ")
numLines(x)
