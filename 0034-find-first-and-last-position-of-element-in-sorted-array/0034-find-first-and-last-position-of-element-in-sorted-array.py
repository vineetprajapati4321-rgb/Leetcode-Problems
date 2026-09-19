class Solution:
    def first_occurrence(self,nums,target):
        low=0
        high=len(nums)-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ans
    def last_occurrence(self,nums,target):
        low=0
        high=len(nums)-1
        ans=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                ans=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return ans
                
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first=self.first_occurrence(nums,target)
        last=self.last_occurrence(nums,target)
        return [first,last]