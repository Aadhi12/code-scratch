# sum of first n numbers using recursion
def sumFunc(n):
    if n<=1: 
        return n
    return n + sumFunc(n-1)
        

# calling function
print(sumFunc(10))  