# print uptill n numbers using backtrack

def printNumbers(n):
    i=1
    def recursion(i,n):
        # base case
        if i>n: 
            return 
        # recursive case
        recursion(i+1,n)
        print(i)
    recursion(i,n)

# calling function
printNumbers(10)  