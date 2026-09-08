class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range (len(nums)):
            hashmap = {} 
            for j in range(i+1,len(nums)):
                r = -(nums[i]+nums[j])

                if r in hashmap :
                    tri = tuple(sorted([nums[i],r,nums[j]]))
                    result.add(tri)
                hashmap[nums[j]] = j
        return [list(x) for x in result]



        