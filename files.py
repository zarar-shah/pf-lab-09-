def numChars(file_name):
    'returns the number of characters in file zarar'
    infile = open(file_name, 'r')
    content = infile.read()
    infile.close()

    return len(content)

x = input("Enter file: ")

numChars(x)
