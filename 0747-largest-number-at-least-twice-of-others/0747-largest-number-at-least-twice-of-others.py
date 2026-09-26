class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            dominant = True

            for j in range(len(nums)):
                if i != j and nums[i] < 2 * nums[j]:
                    dominant = False
                    break

            if dominant:
                return i

        return -1