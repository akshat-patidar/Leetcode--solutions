# time complexity - O(n)
# space complexity - O(1)
# solutions without slow and fast pointer 
class Solution:
    def count(self,head):
        a=0
        current=head
        while current!=None:
            a+=1
            current=current.next
        return int(a)
            
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k=self.count(head)
        if k%2!=0:
            b=k//2
            current=head
            for i in range(b):
                current=current.next
            head=current

            return head
        if k%2==0:
            b=k//2
            current=head
            for i in range(b):
                current=current.next
            head=current
            return head
        