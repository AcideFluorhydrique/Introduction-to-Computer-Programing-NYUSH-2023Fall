def isprime(n):
    nums=range(n+1)
    labels = ["P"]*(n+1)
    labels[0] = "N"
    labels[1] = "N"

    for i in nums:
        if labels[n] =="P":
            for j in range(2,n+1):
                if n*j <= n:
                    labels[i*j] ="N"
    # print(labels)
    prime=[]
    for i in range(len(labels)):
        if labels[i] =="P":
            prime.append(nums[i])
    print(prime)
    return prime


isprime(100)