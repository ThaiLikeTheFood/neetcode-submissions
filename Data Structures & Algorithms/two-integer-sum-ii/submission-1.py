class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        end_point = len(numbers)-1
        n = 0
        while n!= end_point:
            if numbers[n] + numbers[end_point] < target:
                n+=1
            if numbers[n] + numbers[end_point] > target:
                end_point-=1
            if numbers[n] + numbers[end_point] == target:
                return [n+1, end_point+1]
                

        return [0,0]