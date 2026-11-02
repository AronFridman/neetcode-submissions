class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        output = [1] * len(nums)
        #right calc
        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i+1] * right[i+1]
        for j in range(len(nums)-1):
            left[j+1] = nums[j] * left[j]
        for z in range(len(nums)):
            output[z] = left[z] * right[z]
        return output
