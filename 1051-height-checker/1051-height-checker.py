class Solution:
    def heightChecker(self, heights) -> int:
        height=list(heights)
        n=len(height)
        for i in range(0,n):
            for j in range(0,n-1-i):
                if height[j]>height[j+1]:
                    height[j],height[j+1]=height[j+1],height[j]
        count=0
        for i in range(0,n):
            if height[i]!=heights[i]:
                count+=1
        return count
        