class Solution:
    def dominantIndex(self, nums) -> int:
        ind=nums.index(max(nums))
        n=len(nums)
        for i in range(n-1):
            mid=i
            for j in range(i,n):
                if nums[j]<nums[mid]:
                    mid=j
            nums[i],nums[mid]=nums[mid],nums[i]
        for p in range(n-1):
            
            if nums[p]*2>nums[-1]:
                return -1
        return ind
            


        