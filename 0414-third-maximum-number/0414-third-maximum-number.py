class Solution:
    def thirdMax(self, nums) -> int:
        n=len(nums)
        for i in range(n-1):
            mid=i
            for j in range(i+1,n):
                if nums[j]<nums[mid]:
                    mid=j
            nums[i],nums[mid]=nums[mid],nums[i]
        largest=nums[-1]
        count=1
        for p in range(n-2,-1,-1):
            if nums[p]!=largest:
                count+=1
                largest=nums[p]
                if count==3:
                    return nums[p]
        return nums[-1]

        