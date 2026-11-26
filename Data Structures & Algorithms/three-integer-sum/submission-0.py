class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        toReturn = []
        nums.sort()
        seen = set()
        for i in range(len(nums)-2):
            y = i+ 1
            z = len(nums)-1
            while y < z:
                added = nums[i] + nums[y]+ nums[z]
                if added == 0 : 
                    triplet = (nums[i],nums[y],nums[z])
                    if triplet not in seen:
                        toReturn.append([nums[i],nums[y],nums[z]])
                        seen.add(triplet)
                    y += 1
                    z -= 1
                elif added < 0 :
                    y += 1
                else:
                    z -= 1
        return toReturn

