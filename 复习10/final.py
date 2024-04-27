L = [1, 2, 3, 4, 5]
def f(lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            lst.insert(i+1, lst[i])
    return lst
print(f(L))





def new_function(an_int):

    result = ""

    for i in range(an_int):

        x = " " * (an_int - i - 1) + "*" * (i * 2 + 1) + "\n"

        result += x

    for i in range(an_int - 2, -1, -1):

        x = " " * (an_int - i - 1) + "*" * (i * 2 + 1) + "\n"

        result += x

    return result

print(new_function(5))




my_list = [1, 2, 3, 4, 5]
result = [x + y for x in my_list[1:3] for y in my_list[x:]]
print(result)




my_dict = {'apple': 2, 'banana': 3, 'cherry': 5}
total = sum([value for key, value in my_dict.items() if key != 'banana'])
print(total)


set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}

result = set1.update(set2.intersection(set3))
print(result)




def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

result = outer_function(5)(10)
print(result)





def my_function(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"

result = my_function(0)
print(result)




