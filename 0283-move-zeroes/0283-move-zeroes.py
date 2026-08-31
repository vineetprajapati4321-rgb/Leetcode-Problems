class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b=nums.count(0)
        nums[:]=[x for x in nums if x!=0]

        for i in range(b):
            nums.append(0)
        