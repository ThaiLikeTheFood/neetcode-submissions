import numpy as np

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for n, a in enumerate(nums):
            if n > 0 and a == nums[n-1]:
                continue

            prev = nums[n]
            left = n+1
            right = len(nums)-1
            while left < right:
                tot = nums[n]+nums[left]+nums[right]
                if tot > 0:
                    right-=1
                elif tot < 0:
                    left+=1
                else:
                    triplets.append([nums[n],nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
    
        return triplets
        