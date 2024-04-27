# x="global"
# def foo():
#     x=x*2
#     print(x)
# foo()

# def foo():
#     y = "local"
# foo()
# print(y)

a = [1,2,3,4]
b=[5,6]
a.extend(b)
print(a)
print(b)
b.pop()
print(b)

c=[1,2,3,4,5]
c.pop(-2)
print(c)

c[3] = 9
print(c)

l = [2,4,5,6,1,6,8]
for i in l[:]:
    if i % 2 == 0:
        l.remove(i)
print(l)



n = [1,2,3]
m = n
n.append(44)
print(n,m)


def generate_a_3_4_6_3D_array():
    result_lst = []
    for i in range(3):
        result_lst.append([])
        for j in range(4):
            result_lst[i].append([])
            for k in range(6):
                result_lst[i][j].append("*")
    return result_lst
print(generate_a_3_4_6_3D_array())


# def main():
#     J = 10
# main()
# print(main())

def main():
    # Receive user input
    full_name = input("Enter you full name:\n> ")

    #variable to check where the current name starts
    index = 0

    for i in range(len(full_name)):
        if full_name[i] == ' ' or i == (len(full_name) - 1):
            print('{0}. '.format(full_name[index].upper()), end='')
            index = i + 1

# Call the main function.
main()


