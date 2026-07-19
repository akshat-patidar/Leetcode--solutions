# In sorted array
n=len(nums)
l=0
r=n-1

while l<=r:
    mid=(l+r)//2
    if target==nums[mid]:
        return mid
    
    elif target>nums[mid]:
        l=mid+1
        
    else:
        r=mid-1
              
return -1

# nums = [2,3,6,8,10,12,14]
# target = 10