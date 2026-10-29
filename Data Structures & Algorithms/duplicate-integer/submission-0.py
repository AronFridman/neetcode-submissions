class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_check = set(nums)
        if(len(duplicate_check) < len(nums)):
            return True
        return False
    
        