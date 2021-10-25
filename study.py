def open_file(filename):
    try:
        with open(filename) as a_file:
            print("File opening working!")
        
    except:
        print("Something went wrong...")

def odd_lines(filename):
    with open(filename) as a_file:
        lineCounter = 1
        for line in a_file:
            if lineCounter % 2 != 0:
                print(line,end="")
                lineCounter = lineCounter + 1
            else:
                lineCounter = lineCounter + 1


def main():
    #AS1
    open_file(".\study_testFile.txt")

    #AS2
    odd_lines(".\study_testFile.txt")

if __name__ == "__main__":
    main()
