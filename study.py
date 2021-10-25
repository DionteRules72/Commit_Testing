def open_file(filename):
    try:
        with open(filename) as a_file:
            print("File opening working!")
        
    except:
        print("Something went wrong...")

def main():
    open_file(".\study_testFile.txt")
if __name__ == "__main__":
    main()
