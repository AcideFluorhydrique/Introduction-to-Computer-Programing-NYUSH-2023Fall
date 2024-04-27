# def is_digit(n):
#     return n.isdigit()



def is_digit(s):
    for c in s:
        if c not in "0123456789":
            return False
    return True