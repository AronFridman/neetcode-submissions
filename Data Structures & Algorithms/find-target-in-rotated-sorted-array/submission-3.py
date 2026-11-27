class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l < r :
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]:
                l = mid + 1 
            else:
                r = mid
        if(l == 0):
            r = len(nums) -1
        
        elif target >= nums[0]:
            r -= 1
            l = 0
        else:
            r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1 
            else:
                r = mid -1 
        return -1