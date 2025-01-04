'''You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1,1]
        for i in range(2, n+1):
            fib.insert(i, (fib[i - 1] + fib[i - 2]))
        return fib[n]
