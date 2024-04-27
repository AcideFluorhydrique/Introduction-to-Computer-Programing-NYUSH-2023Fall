import random

a = random.randint(1,14)
b = random.randint(1,14)
c = random.randint(1,14)
d = random.randint(1,14)

print("a =", a)
print("b =",b)
print("c =",c)
print("d =", d)

# ***********

print("********")


def solve_24(nums):

    if len(nums) == 1:
        if nums == 24: 
            return True
        else:
            return False
        
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i != j:
                new_nums = [nums[k] for k in range(0, len(nums)) if (k != i and k != j)]
                new_nums.append(nums[i] + nums[j])
                if solve_24(new_nums):
                    return True
                new_nums.pop()
                new_nums.append(nums[i] - nums[j])
                if solve_24(new_nums):
                    return True
                new_nums.pop()
                new_nums.append(nums[i] * nums[j])
                if solve_24(new_nums):
                    return True
                new_nums.pop()
                new_nums.append(nums[i] / nums[j])
                if solve_24(new_nums):
                    return True
                new_nums.pop()
    return False

nums_to_solve = [a,b,c,d]
result = solve_24(nums_to_solve)

if result:
    print("可解")
else:
    print("无解！")

# if result:
    
