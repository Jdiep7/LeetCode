def TopDownfib(n):
    memo = {0:0, 1:1}
    
    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
        
    return f(n)

def BottomUpfib(n):
    dp = [0]*(n+1)

    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
        
    return dp[n]

print(BottomUpfib(8))
    