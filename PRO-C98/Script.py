#Setup
def replaceTextFromTwoFiles():
    fileName1 = input("Enter First File: ")
    fileName2 = input("\nEnter Second File: ")

    file1 = open(fileName1, 'r')
    file1txt = file1.read()
    print("\n", file1txt)

    file2 = open(fileName2, 'r')
    file2txt = file2.read()
    print(file2txt, "\n")

    file1.close()
    file2.close()

    file1 = open(fileName1, 'w')
    file2 = open(fileName2, 'w')

    file1.write(file2txt)
    file2.write(file1txt)

    file1.close()
    file2.close()

    file1 = open(fileName1, 'r')
    file2 = open(fileName2, 'r')

    result1txt = file1.read()
    print(result1txt)

    result2txt = file2.read()
    print(result2txt)

    file1.close()
    file2.close()


#Display
for i in range(1, 2):
    print("\n")

    replaceTextFromTwoFiles()

for i in range(1, 2):
    print("\n")