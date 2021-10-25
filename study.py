def open_file(filename):
    try:
        with open(filename) as a_file:
            print("File opening working!")
        
    except:
        print("Something went wrong...")

def oddLines_totalLines(filename):
    lineCounter = 1
    with open(filename) as a_file:
        for line in a_file:
            if lineCounter % 2 != 0:
                print(line,end="")
                lineCounter = lineCounter + 1
            else:
                lineCounter = lineCounter + 1
    return lineCounter
    



def main():
    #AS1
    open_file(".\study_testFile.txt")

    #AS2 - AS3
    oddLines_totalLines(".\study_testFile.txt")
    aliceTotalLines = oddLines_totalLines(".\data\\alice.txt")
    print("Number of lines in 'alice.txt' is",aliceTotalLines)

if __name__ == "__main__":
    main()
