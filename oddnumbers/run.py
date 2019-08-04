def oddNumbers(l, r):
    result = []
    for num in  range(l,r+1):
        if num % 2 != 0:
           result.append(num)  
    return result