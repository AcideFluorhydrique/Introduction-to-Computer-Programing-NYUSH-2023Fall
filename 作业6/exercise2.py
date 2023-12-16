# """
# PROGRAMMING ASSIGNMENT 06
# Filename: 'exercise2.py'

# The file 'exercise2.py' is a module that offers functions for managing a list of users and their
# passwords.
# The usernames and passwords are stored in a list of lists that we will name userList.
# Each inner list represents a username/password pair in that order [username, password].
# """

# # Place your imports here if any


# def valid_username(user, L):
#     """
#     1. Displays a message (Valid , Invalid or User Name Exists) depending on username rules
#     2. Returns if the username is valid → type bool
#     """
#     # WRITE YOUR CODE BELOW
#     if len(user) < 4:
#         print("Invalid")
#         return False
#     elif user[0].isdigit():
#         print("Invalid")
#         return False
#     elif not(user.isalnum()):
#         print("Invalid")
#         return False
#     elif user in L:
#         print("User Name Exists")
#         return False
#     else:
#         print("Valid")
#         return True

# def valid_password(pwd):
#     """
#     1. Displays a message ( Valid or depending on password rules
#     2. Returns if the password is valid → type bool
#     """
#     # WRITE YOUR CODE BELOW
#     if len(pwd) < 10:
#         print("Invalid")
#         return False
#     elif not(pwd.isalnum()):
#         print("Invalid")
#         return False
#     elif not(any(i.islower() for i in pwd)):
#         print("Invalid")
#         return False
#     elif not(any(i.isupper() for i in pwd)):
#         print("Invalid")
#         return False
#     elif not(any(i.isdigit() for i in pwd)):
#         print("Invalid")
#         return False
#     else:
#         print("Valid")
#         return True
    
# def add_user(L):    
#     """
#     1. Continuously ask the user to input a username, until it is a valid one
#     2. Ask for a password with the following logic:
#         (a) continuously ask the user to input a password, until it is a valid one
#         (b) ask the user to input the password again:
#             • if the 2 passwords match → move to 3.
#             • otherwise → display `Passwords do not match` and go back to 2.(a)
#     3. Add the username/password pair to the userList and display User created
#     """
#     # WRITE YOUR CODE BELOW
#     user = input("Enter Username: ")
#     while not(valid_username(user, L)):
#         user = input("Enter Username: ")

#     pwd = input("Enter Password: ")
#     while not(valid_password(pwd)):
#         pwd = input("Enter Password: ")

#     print('User created')
#     new = [user,pwd]
#     L.append(new)

    
# # DO NOT CHANGE THE CODE BELLOW
# if __name__ == '__main__':
#     userList = [['sunny1', 'pwd1DdeEff'], ['superS', 'pwD2Abcdefgh'],
#     ['likeA', 'pwd3AAAAAA'], ['qwerty', 'pwd4QWERTY']]

#     add_user(userList)

#     print(userList)



"""
PROGRAMMING ASSIGNMENT 06
Filename: 'exercise2.py'

The file 'exercise2.py' is a module that offers functions for managing a list of users and their
passwords.
The usernames and passwords are stored in a list of lists that we will name userList.
Each inner list represents a username/password pair in that order [username, password].
"""

# Place your imports here if any


def valid_username(user, L):
    """
    1. Displays a message (Valid , Invalid or User Name Exists) depending on username rules
    2. Returns if the username is valid → type bool
    """
    # WRITE YOUR CODE BELOW
    if len(user) < 4:
        print('Invalid')
        return False
    if not user.isalnum():
        print('Invalid')
        return False
    temp=user[0]
    if temp.isdigit():
        print('Invalid')
        return False
    for i in L:
        if user == i[0]:
            print('User Name Exists')
            return False
    print('Valid')
    return True

    
def valid_password(pwd):
    """
    1. Displays a message ( Valid or depending on password rules
    2. Returns if the password is valid → type bool
    """
    # WRITE YOUR CODE BELOW
    if len(pwd) < 10:
        print('Invalid')
        return False
    elif not pwd.isalnum():
        print('Invalid')
        return False
    elif pwd.isalpha():
        print('Invalid')
        return False
    elif pwd.upper() == pwd or pwd.lower() == pwd:
        print('Invalid')
        return False
    print('Valid')
    return True


def add_user(L):
    """
    1. Continuously ask the user to input a username, until it is a valid one
    2. Ask for a password with the following logic:
        (a) continuously ask the user to input a password, until it is a valid one
        (b) ask the user to input the password again:
            • if the 2 passwords match → move to 3.
            • otherwise → display `Passwords do not match` and go back to 2.(a)
    3. Add the username/password pair to the userList and display User created
    """
    # WRITE YOUR CODE BELOW
    b1 = True; b2 = True
    while b1:
        username = input('Enter Username: ')
        b1 = not valid_username(username,L)
    while b2:
        pwd = input('Enter Password: ')
        if valid_password(pwd):
            C = input('Confirm Password: ')
            if C == pwd:
                global userList
                userList.append([username,pwd])
                print('User created')
                break
            else:
                print('Passwords do not match')
                continue
        else:
            continue

# DO NOT CHANGE THE CODE BELLOW
if __name__ == '__main__':
    userList = [['sunny1', 'pwd1DdeEff'], ['superS', 'pwD2Abcdefgh'],
    ['likeA', 'pwd3AAAAAA'], ['qwerty', 'pwd4QWERTY']]

    add_user(userList)

    print(userList)
