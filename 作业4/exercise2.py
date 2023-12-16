"""
Blackjack is a card game played with one or several standard 52-card decks. The value of the
cards is calculated regardless of suits or colors. We will only use letters and digits to indicate the
different cards: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K. The object of the game is to reach 21 points or
to get as close to 21 points without going higher. The value of cards two through ten is their pip
value (2 through 10). Face cards (Jack, Queen, and King) are each worth ten. Aces can be worth
one or eleven , whichever is better for the player. A hand's value is the sum of the card values.
Players are allowed to draw additional cards to improve their hands.

Each player has some cards in his hand. They must then make a decision of whether to Hit or
Stay. Hit means they request an additional card, Stay means they stop with their current total.
Players generally try to Hit until it is likely that another card will push them over 21. For example,
if a player has a 5 and a 7, there is a relatively low chance that another card would push them over
21 (only J, Q, and K would do so, since 12 + 10 = 22).On the other hand, if they have a 5, a 6,
and a 7, they will likely stay because any card above 3 will push them over 21 points.
"""

# The rules are:
# • The dealer must Hit if their total is below 17.
# • The dealer must Stay as soon as their total is 17 or higher.
# • An Ace (A) should be counted as 11 if it puts the dealer between 17 and 21 points. If it puts
# them over 21, though, it should be counted as 1.


"""
Write a program that does the following:
1. ask the user to enter his hand
2. then print out:
(a) ”Hit” if the dealer should take another card.
(b) ”Stay” if the dealer should not take another card.
(c) ”Bust” if the sum is already over 21.

"""



x = input("Enter your hand: > ")
S = 0
A = 0
for i in range(0,len(x)):
#老K、皮蛋、夹勾 都应该被看作 10
    if x[i] == "J" or x[i] == "Q" or x[i] == "K" or x[i] == "1" :
#怎么解决10？？ 或许直接把 0 忽略也不是不行
        S += 10
    elif x[i] == "2" :
        S = S + 2
    elif x[i] == "3" :
        S = S + 3
    elif x[i] == "4" :
        S = S + 4
    elif x[i] == "5" :
        S = S + 5
    elif x[i] == "6" :
        S += 6
    elif x[i] == "7" :
        S = S + 7
    elif x[i] == "8" :
        S = S + 8
    elif x[i] == "9" :
        S += 9
#爱斯不好搞 先把 A 的数量记录下来
    elif x[i] == "A" :
        A += 1

#先解决读取卡牌的问题 ↑

#接下来我应该是要解决爱斯的分配 到底是 1 还是 11
"""
while A >= 1:
    if (S + 11) > 21:
        S += 1
        A -= 1
    elif (S + 11) >= 17 and (S + 11 ) <= 21:
        S += 11
        A = A - 1
"""
#很离谱 如果A太多的话 这里会出bug？？unknown reason#
#What if there are more than four "Aces" ?

"""
如果有k个Ace,先检查如果k个A都是1可不可以,
可以的话再检查一个爱斯是11,其余为1可不可以,然后检查两个A为11其余为1.
对于AAAA8,s初始为8。这里我直接贪心,想尽可能塞11.
但第一次进入循环时elif条件成立,s+=11,但其实这四个A都应视作1
"""

j = 0
while S + j * 11 + (A-j)*1 < 11:
    j += 1
S = S + j * 11 + (A-j)*1


    # if S + j * 11 + (A-j)*1 > 21:
    #     break
    # else:
    #     S = S + j * 11 + (A-j)*1 
# ↑ wrong

if S < 17:
    print("Hit")
elif S > 21:
    print("Bust")
else:
    print("Stay")
