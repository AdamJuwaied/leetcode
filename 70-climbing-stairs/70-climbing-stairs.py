class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Current last two sums of steps to possibly take
        step1, step2 = 1, 1
        
        # Working bottom up. Getting n and n-1 = 1, then adding them to get fib numbers
        for i in range((n) - 1):
            temp = step1
            step1 = step1 + step2
            step2 = temp
            
        return step1
        