

def chop(list):
    del list[0]
    n = len(list)
    del list[n-1]
    return None

num = [1,2,3,4,5,6,7]
chop(num)    
print(num)