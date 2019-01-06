def numWords(filename):
    'return the number of words in file filename'
    infile = open(filename, 'r')
    content = infile.read()           #read the file into a string
    infile.close()


    wordList = content.split()    #split file into list of words
    print(wordList)              #print list of words too
    return len(wordList)

x = input("Enter file: ")

numWords(x)