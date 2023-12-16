"""
PROGRAMMING ASSIGNMENT 08
Filename: 'exercise1.py'
"""
# Place your imports here if any

def build_attraction_dict(filename):
    """
    Read from the file for which the filename was given and returns a dictionary

    The key / value pairs in the dictionary will be:
        • key → attraction name (str type)
        • value → Province (str type)
    """
    # TODO

    f = open(filename,"r")
    content = f.readlines()
    dic = {}
    for line in content[:]:
        k,v = (line.strip()).split(",")
        dic[v] = k

    # dic = {}
    # with open(filename,"r") as f:
    #     for line in f:
    #         k,v = map(str.strip, line.split(","))
    #         dic[k] = v

    # print(pc)

    f.close()
    return dic



def add_attraction(dic):
    """
    This function takes a dictionary as a parameter and does not return anything.

    The function:
        • asks the user to input an attraction name
        • asks the user to input a province
        • updates the dictionary with a new key / value pair (with a similar format for
        task 1)
    """
    # TODO

    attraction = input("Input a new attraction: ")
    province = input("Input the province: ")
    dic[attraction] = province


def build_province_attraction_dict(dic):
    """
    This function takes a dictionary as a parameter and returns another dictionary.

    The input dictionary is constituted of key / value pairs similar to the ones built in task 1.

    The returned dictionary should have key / value pair with:
        • key → Province (str type)
        • value → list of attraction names (list of str type) associated to the Province
    """
    # TODO

    New = {}
    for attraction, province in dic.items():
        if province in New:
            New[province].append(attraction)
        else:
            New[province] = [attraction]

    # print(New) 
    return New


def most_attractions(dic):
    """
    This function takes a dictionary as a parameter and returns a set.

    The input dictionary is constituted of key / value pairs similar to the ones built in task 3.

    The returned set should contain the Provinces which have at least 3 tourist attractions
    (in the input dictionary).
    """
    # TODO

    province_set = set()
    for province, attraction in dic.items():
        if len(attraction) > 2:
            province_set.add(province)

    # print(province_set)

    return province_set




def main():
    """
    The main() function will
        1. calls `build_province_attraction_dict` with filename top_tourist_attractions.txt as 
            parameter to generate the first dictionary.
        2. calls `add_attraction` one time in order to update the dictionary. The user will input
            a new (non-existing) attraction name/Province pair.
        3. calls `build_province_attraction_dict` in order to generate a second dictionary.
        4. calls `most_attractions` in order to generate the set of Provinces with at least 3 attractions.
        5. prints the Provinces with at least 3 attractions. Display one Province per line.
            See sample examples for the proper format (empty line + Header line).
            
    """
    # TODO

    first_dic = build_attraction_dict("top_tourist_attractions.txt")
    add_attraction(first_dic)
    second_dic = build_province_attraction_dict(first_dic)
    province_set = most_attractions(second_dic)

    # print()
    print("\nProvinces with at least 3 attractions:")
    for province in province_set:
        print(province)


if __name__ == '__main__':
    main()
