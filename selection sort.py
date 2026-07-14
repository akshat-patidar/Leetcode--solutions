class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # time complexity - O(n^2)
        # space complexity - O(1)
        n=len(nums)
        for i in range(n):
            mn=nums[i]
            ind=i
            for j in range(i+1,n):
                if nums[j]<mn:
                    mn=nums[j]
                    ind=j
            temp=nums[i]
            nums[i]=nums[ind]
            nums[ind]=temp
        return nums

    # input  [5,2,3,1]
    # output  [1,2,3,5]
        