# print uptill n numbers

def printNumbers(n):
    i=1
    def recursion(i,n):
        # base case
        if i>n: 
            return n
        print(i)
        # recursive case
        recursion(i+1,n)
    recursion(i,n)

# calling function
printNumbers(10)   