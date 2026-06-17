class Solution:

    def solution(self, nums: list[int], target: int) -> list[int]:

        temp = {}
        ans = []

        l = len(nums)
        for i in range(l):
            temp[target-nums[i]]=i
        
        for i in range(l):
            if nums[i] in temp and i != temp[nums[i]]:
                ans.append(i)
                ans.append(temp[nums[i]])
                break

        return ans

