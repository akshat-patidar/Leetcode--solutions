#  inssertion sort
#  time complexity-O(n^2)
#  space complexity-O(1)

class Solution:
    def sort(self,nums):
        n=len(nums)
        for i in range(1,n):
            key=nums[i]
            j=i-1
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums
    
s=Solution()
print(s.sort([2,3,8,1,7]))
#output  [1,2,3,7,8]
