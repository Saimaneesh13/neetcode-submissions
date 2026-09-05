class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = set(nums)
        n = len(nums)
        longest = 0
        for i in range(n):
            if nums[i]-1 not in lst:
                first = 1
                current = nums[i]
                while current + 1 in lst:
                    current +=1
                    first +=1
                longest = max(longest,first)
        return longest



