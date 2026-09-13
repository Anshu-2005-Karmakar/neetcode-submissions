class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [] 
        l = [] 
        l.append(1)
        for i in range(1,len(nums)):
            l.append(l[i-1] * nums[i-1])
        r = [1] * len(nums) 
        for j in range(len(nums)-2,-1,-1):
            r[j] = r[j+1] * nums[j+1]
        for k in range(len(nums)):
            ans.append(l[k] * r[k])
        return ans