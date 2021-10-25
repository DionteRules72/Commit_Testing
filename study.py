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

def even_letters(filename):
    final_str = " "

    with open(filename) as a_file:
        iterationStop = 30
        letterCounter = 0
        every = 20
        for line in a_file:
            lines = line.split(" ")
            for word in lines:
                words = word.split()
                for letter in words:
                    if iterationStop <= 0:
                        break
                    else:
                        if letterCounter % 2 == 0:
                            print(letter,end="")
                            letterCounter = letterCounter + 1
                        else:
                            letterCounter = letterCounter + 1

    return final_str

def main():
    #AS1
    open_file(".\study_testFile.txt")

    #AS2 - AS3
    oddLines_totalLines(".\study_testFile.txt")
    aliceTotalLines = oddLines_totalLines(".\data\\alice.txt")
    print("Number of lines in 'alice.txt' is",aliceTotalLines)
    
    #AS4
    even_letters(".\data\\alice.txt")



if __name__ == "__main__":
    main()
