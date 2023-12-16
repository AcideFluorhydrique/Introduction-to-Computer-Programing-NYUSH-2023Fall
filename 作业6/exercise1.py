# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise1.py'
#
# See instructions in pdf file
#

def clean_users(L):
    """• input: 1 parameter L -> type list (of strings) - each element in the list is a username
• return: a new cleaned list (see the rules below) -> type list (of strings)

The logic for cleaning the list of usernames is:
    • if the username contains c, g or z, it should be removed (the same with C, G or Z)
    • otherwise, keep it in the list

Note: your function should not modify the original list!"""
    # WRITE YOUR CODE BELOW

    # for i in range(5):
    #     if "c" in L[i] or "g" in L[i] or "z" in L[i]:
    #         del L[i]
    # return L

    # for i in L:
    #     if "c" in i or "g" in i or "z" in i or "C" in i or "G" in i or "Z" in i:
    #         L.remove(i)
    # return L
    # ↑ 上面俩似乎不行
    cleaned = [c for c in L if not any(char in c for char in 'cgzCGZ')]
    return cleaned
    
def main():
    """The program does the following:
    1) asks the user to input 5 usernames (only alphanumeric characters will be input,
       no space, no underscore, ...) and stores them into a list
    2) prints out the list of usernames
    3) calls clean_users function to clean the list
    4) prints out the cleaned list"""
    # WRITE YOUR CODE BELOW
    
    a = input("username: ")
    b = input("username: ")
    c = input("username: ")
    d = input("username: ")
    e = input("username: ")

    List = [a,b,c,d,e]
    List_copy = List
    print(List)
    CleanedList = clean_users(List_copy)
    print(CleanedList)

#Call the main() function, DO NOT CHANGE THE CODE BELLOW
if __name__ == '__main__':
    main()
