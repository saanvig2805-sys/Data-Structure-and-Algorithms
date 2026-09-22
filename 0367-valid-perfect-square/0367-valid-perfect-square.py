class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start=0
        end=num
        ans=0
        while start<=end:
            mid=(start+end)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                ans=mid
                start=mid+1

            else:
                end=mid-1
        return False