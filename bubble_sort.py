class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # time complexity - O(n^2)
        #space complexity - O(1)
        for i in range(n-1):
            swap=False
            for j in range(n-1-i):
                if nums[j+1]<nums[j]:
                    temp=nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
                    swap=True
            if not swap:
                break
        return nums
 # Example:
# Input: [5, 2, 3, 1]
# Output: [1, 2, 3, 5]