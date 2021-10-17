class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2 
            else:
                num -=1 
            steps += 1
        return steps

ans = Solution()
print(ans.numberOfSteps(14))
print(ans.numberOfSteps(8))
        