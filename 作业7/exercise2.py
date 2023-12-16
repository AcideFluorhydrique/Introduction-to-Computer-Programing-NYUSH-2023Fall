"""
PROGRAMMING ASSIGNMENT 06
Filename: 'exercise2.py'

Write a program (in the main() in exercise2.py) which:
    1. asks the user to input a filename (supposedly in the same folder as your program)
    2. reads the numbers (type int ) in the file (filename given by the user in previous step)
    and stores them into a list
    3. prints the minimum, the maximum and the average of the numbers (2 decimal places for the average)

Note: Your program should be impossible to crash.
      Think about all the possibilities to make your program crash.
      If one of the steps throws an exception,
        display a message to the user and your program should loop back to step 1.

Output: If the file cannot be found, display "File not found".
        For the rest of the exception, simply display "Error".

"""
import decimal
# Place your imports here if any

def main():
    B = False
    """Implement the logic according to instructions"""
    
    while not(B):
        name = input("Filename:\n")
        try:
            f = open(name,"r")
            L = f.readlines()
            # print(L)
            
            try:
                numbers = []
                for i in L:
                    numbers.append(int(i))
                    
                Min = min(numbers)
                Max = max(numbers)
                Ave = sum(numbers) / len(numbers)
                print("Minimum:",Min)
                print("Maximum:",Max)
                print("Average:",'%.2f' % Ave)
                B = True
            except:
                print("Error")
                B = False
                            
        except:
            print("File not found")
    
if __name__ == '__main__':
    main()
