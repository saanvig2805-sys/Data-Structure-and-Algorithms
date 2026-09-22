# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start=1 #because its given range is from 1 
        end=n
        while start<=end:
            mid=(start+end)//2
            if isBadVersion(mid):
                end=mid-1
            else:
                start=mid+1
        return start #only start will run because if we will return end the the if staement will give the previous iteration
            
            