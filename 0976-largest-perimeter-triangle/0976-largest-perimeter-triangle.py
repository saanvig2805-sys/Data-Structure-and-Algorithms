class Solution:
    def largestPerimeter(self, nums) -> int:
        nums.sort()
        n=len(nums)
        # for i in range(n-1):
        #     mid=i
        #     for j in range(i,n):
        #         if nums[j]<nums[mid]:
        #             mid=j
            # nums[i],nums[mid]=nums[mid],nums[i]
        for p in range(n-1,1,-1):
            # left=p-2
            # right=p-1
            if nums[p-1]+nums[p-2]>nums[p]:
                # left=right
                # right=right+1
                return nums[p-1]+nums[p-2]+nums[p]
        return 0

    
        

        