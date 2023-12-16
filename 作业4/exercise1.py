"""
Write a program (in the file exercise1.py) that does the following:

1. Ask the user how many words, between 3 and 6, he will enter
2. Ask the question until the user enter a number between 3 and 6
3. Proceed to ask for each word, one at a time: Word #[number] please >
4. At the end, your program should print out:
(a) the shortest word (the most recently entered shortest if there is a tie)
(b) the longest word (the most recently entered longest if there is a tie)
(c) the average length of all of the words (up to the second decimal point)

"""

# x = []
# number = int(input("How many words will you enter? > "))
# while number >= 7 or number <= 2:
#     print("Invalid input. Please enter a number between 3 and 6")
#     number = int(input("How many words will you enter? > "))
# for k in range(1,number+1):
#     word = input(f"Word #{k} please > ")
#     x.append(word)
# def wordlength(word):
#     return len(word)
# shortest_word = min(x, key=wordlength)
# longest_word = max(x, key=wordlength)
# total_length = sum(len(word) for word in x)
# average_length = total_length / number
# print("Shortest:",shortest_word)
# print("Longest:",longest_word)
# print("Average Length:",'%.2f'%average_length)

"""
以上似乎不能解决长度相同时的次序问题
"""


number = int(input("How many words will you enter? > "))
while number >= 7 or number <= 2:
    print("Invalid input. Please enter a number between 3 and 6")
    number = int(input("How many words will you enter? > "))
total = 0
longest = ""
#如何把shortest初始值设为无穷大 ∞ ？？
#float("inf")
#这是一个问题
shortest = ""
for k in range(1,number+1):
    word = input(f"Word #{k} please > ")
    if len(word) >= len(longest) or longest == "":
        longest = word
    if len(word) <= len(shortest) or shortest == "":
        shortest = word
    #用新的替代旧的 解决长度相同时的次序问题
    total = total + len(word)
average_length = total / number
print("Shortest:",shortest)
print("Longest:",longest)
print("Average Length:",'%.2f'%average_length)