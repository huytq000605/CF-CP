import bisect
from collections import Counter

def sol(arr):
    arr+=[float('inf')]
    presum=[0]
    for i in arr: presum+=[presum[-1]+i]   

    dp = [0 for _ in range(len(arr) + 1)]

    n, prev, cur = len(arr)-1, Counter(),0

    for i in range(n):

      i+=1

      cur=max(cur,prev[i])

      dp[i]=(i-cur-1) + dp[cur]

      idx=bisect.bisect_left(presum,2*presum[i]-presum[cur])   

      prev[idx]=i

    print(dp)
    print(prev)
    return n-dp[n]

sol([ 1, 2, 1, 3, 3 ])
