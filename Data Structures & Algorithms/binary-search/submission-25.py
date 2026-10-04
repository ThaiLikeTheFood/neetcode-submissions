class Solution:
    def search(self, nums: List[int], target: int) -> int: 
        idx = int(len(nums)/2)
        while target != nums[idx]:
            print(idx)
            if nums[idx] > target and nums[idx-1] < target:
                return -1
            if target > nums[idx]:
                idx+=1
                if idx >= len(nums):
                    return -1
            elif target < nums[idx]:
                idx-=1
                if idx < 0:
                    return -1
            else:
                return -1
        return idx

    
        