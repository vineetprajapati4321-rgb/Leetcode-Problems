class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            res=0
            k=str(nums[i])
            for j in k:
                j=int(j)
                res+=j
            if res==i:
                return i
        return -1