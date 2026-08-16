class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif  target<nums[0]:
            return 0
        
        elif len(nums)==1 and target>=nums[0]:
            return 1
        else:
            for i in range(0,len(nums)-1):
                if nums[i]<target<nums[i+1]:
                    return nums.index(nums[i+1])
            else:
                return len(nums)