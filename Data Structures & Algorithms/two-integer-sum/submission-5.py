class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mySet = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            complement = target - nums[i]
            if ((complement in mySet) and(i!=mySet[complement])):
                return [i, mySet[complement]]
            mySet[nums[i]] = i


            
            

            
        