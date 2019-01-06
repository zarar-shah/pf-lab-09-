def distribution(filename):
    infile=open(filename, 'r')
    alltext=infile.read()
    infile.close()

    splitwords = alltext.split()

    aplus=0
    a=0
    bplus=0
    b=0
    c=0
    d=0
    f=0

    for grades in splitwords:
        if grades== "A+":
            aplus+=1
        elif grades == 'A':
            a+=1
        elif grades == "B+":
            bplus+=1
        elif grades =='B':
            b+=1
        elif grades == 'C':
            c+=1
        elif grades == 'D':
            d+=1
        elif grades == 'F':
            f+=1

    print("Students got A+:",aplus,"\nStudents got A", a, "\nStudents got B+:", bplus, "\nStudents got B:", b,"\nStudents got C:",c, "\nStudents got D:", d, "\nStudents got F:",f)

file=input("Enter file: ")
distribution(file)




