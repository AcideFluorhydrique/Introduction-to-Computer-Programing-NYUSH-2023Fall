"""
PROGRAMMING ASSIGNMENT 06
Filename: 'exercise1.py'

Suppose we have two text files file1.txt and file2.txt in the same folder
as your python program (you can download the sample files on NYU Classes
and put it in the same folder as your program, or create your own text files).

Write a program (in the main() in exercise1.py) 
which inserts all the content from file2.txt to the beginning of file1.txt.

After executing your program, only file1.txt will be updated, file2.txt will not change.

# Place your imports here if any
"""


def main():
    """Implement the logic according to instructions"""
    f = open("file1.txt","r")
    i = ""
    while True:
        line = f.readline()
        if line:
            i += line
        else:
            break
    # print(i)
    g = open("file2.txt","r")
    j = ""
    while True:
        line = g.readline()
        if line:
            j += line
        else:
            break
    # print(j)
    new = j + i
    # print(new)
    h = open('file1.txt','w')
    h.write(new)
    
if __name__ == '__main__':
    main()