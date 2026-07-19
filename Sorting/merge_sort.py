# time complexity - O(nlog(n))
#space complexity - O(n)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
        #base case
            if len(nums)<=1:
                return nums
        #recursive case
            mid=len(nums)//2
            left=merge_sort(nums[:mid])
            right=merge_sort(nums[mid:])

            return merge(left,right)

        def merge(left,right):
            result=[]
            i=0
            j=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    result.append(left[i])
                    i+=1

                else:
                    result.append(right[j])
                    j+=1
            while i<len(left):
                result.append(left[i])
                i+=1

            while j<len(right):
                result.append(right[j])
                j+=1

            return result 
        return merge_sort(nums)
        
 # example [5,6,4,3,1]
 # output [1,3,4,5,6]
    