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
import os

def main(fn):
    """Implement the logic according to instructions"""
    f = open(fn,"r")
    with open(fn, "r") as f:
        x = f.read()
        print(x)#测试失败

if __name__ == '__main__':
    cur_dir = os.getcwd()
    fn = "file2.txt"
    full_fn = os.path.join(cur_dir, "作业7",fn)

    print ("=-=-=-==-=--")
    print(full_fn)
    print("##########")
    main(fn)
