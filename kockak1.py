MOD = 10**9 + 7

def count_ways(n):
   
    dp = [0] * (n + 1)
    dp[0] = 1 

    rolling_sum = dp[0]
    
    for i in range(1, n + 1):
      
        dp[i] = rolling_sum
       
        rolling_sum = (rolling_sum + dp[i]) % MOD
        if i >= 6:
            rolling_sum = (rolling_sum - dp[i - 6]) % MOD
    
    return dp[n]


n = int(input())

print(count_ways(n))
