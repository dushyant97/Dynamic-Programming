# Top down approach or Memorization method
def topdown_fib(n):
    if (already_fib[n-1]!= -1):
        return already_fib[n]
    else:
        if(n==1):
            return 1
        elif(n==0):
            return 0
        else:
            result = topdown_fib(n-1) + topdown_fib(n-2)
            already_fib[n-1] = result
            return result
        
# Bottom Up Apporach or Tabulation Method
def bottomup_fib(n):
    a={}
    a[0]=0
    a[1]=1
    for i in range(2,n+1):
        a[i]=a[i-1] + a[i-2]
    return a[n]        
    
x = int(input("Enter the number\n"))
already_fib=[-1]*x
print("The %dth fibonacci number is "% x, topdown_fib(x))
