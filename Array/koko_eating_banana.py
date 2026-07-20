class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        l=1(
        r=max(piles)
        
        while l<=r:
            count=0
            mid=(l+r)//2
    
            for i in piles:
                count+=i+mid-1)//mid
            if count>h:
                l=mid+1
            else:
                r=mid-1
        return l