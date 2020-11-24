#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?


#my solution
lst = [10, 30, 6, 7]
k = 36

def funct(lst, k):
    for i in lst:
        for j in lst:
            if i != j:
                if (i + j) == k:
                    return(True)
    else:
        return(False)

print(funct(lst, k))
                   
#set solution, less time complexity since traversing set  https://stackoverflow.com/questions/51300360/given-a-list-of-numbers-and-a-number-k-return-whether-any-two-numbers-from-the  
st = set(10, 30, 6, 7)
k = 36

def funct(lst, k):
    for i in st:
        if (k - i) in st:
            return(True)
    else:
        return(False)

print(funct(st, k))

#sort solution
lst = [10, 30, 6, 7]
k = 36

def funct(lst, k):
    lst.sort()
    i = 0
    j = len(lst) - 1
    while i < j:
        sum = lst[i] + lst[j]
        if sum < k:
            i += 1
        elif sum > k:
            j -= 1
        else:
            return(True)
    return(False)

print(funct(lst, k))