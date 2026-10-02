class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        setLen = len(my_set)
        for i in range(len(nums)):
            my_set.add(nums[i])
            if len(my_set) == setLen:
                return True
            else:
                setLen+=1
        return False
            
                

        
        