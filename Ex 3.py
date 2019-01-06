print("Name: Zarar Ali Shah")
print("Roll #:18B-075-CS (A)")
print("LAB 09")

def duplicate(filename):
    infile=open(filename, 'r')
    alltext = infile.read()
    splitwords=alltext.split()
    infile.close()

    list=[]
    textcount=0
    for chars in splitwords:
        list.append(chars)
        if list.count(chars) >1:
            textcount=+1
        if textcount>0:
            print("TRUE")
        else:
            print("FALSE")

a=input("Enter file: ")
duplicate(a)


