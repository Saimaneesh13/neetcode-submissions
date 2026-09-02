class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        n = len(nums)
        pref = []
        pref.append(nums[0])
        sufix = [0]*n
        sufix[n-1] = nums[n-1]
        final = []
        for i in range(1,len(nums)):
            pref.append(pref[i-1]*nums[i])
        for i in range(n-2,-1,-1):
            sufix[i]=sufix[i+1]*nums[i]
        for i in range(n):
            left = pref[i-1] if i>0 else 1
            right = sufix[i+1] if i<n-1 else 1
            final.append(left*right)
        return list(final)
