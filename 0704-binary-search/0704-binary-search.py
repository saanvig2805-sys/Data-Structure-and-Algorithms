class Solution:
    def search(self,nums, target) -> int:
        start=0
        size=len(nums)
        end=size-1
        
        while(start<=end):
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                start=mid+1
            elif nums[mid]>target:
                end=mid-1
        return -1
    