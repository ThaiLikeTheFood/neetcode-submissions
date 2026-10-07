class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        best = -1
        while left < right:
            score = self._compute_score(left, right, heights)
            best = max(best,score)

            if heights[left] < heights [right]:
                left+=1
            else:
                right-=1

        return best
        
        
        

    def _compute_score(self, left, right, heights):
        span = right - left
        scoring = min(heights[left],heights[right])
        return span*scoring
        