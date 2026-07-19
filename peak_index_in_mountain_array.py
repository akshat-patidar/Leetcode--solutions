# time complexity - O(log(n))
# space complexity - O(1)
# difficulty level - medium
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        l=0
        r=n-1
        
        while l<=r:
            mid=(l+r)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid

            elif arr[mid+1]>arr[mid]:
                l=mid+1
            else: 
                r=mid-1

        
            
        