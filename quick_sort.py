# time complexity -- O(n^2)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(low, high):

            # Base Case
            if low >= high:
                return

            
            key = nums[high]

            i = low - 1

            
            for j in range(low, high):

                if nums[j] < key:

                    i = i + 1

                    # Swap using temp
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

            
            temp = nums[i + 1]
            nums[i + 1] = nums[high]
            nums[high] = temp

            pos = i + 1

            # Left part
            quick_sort(low, pos - 1)

            # Right part
            quick_sort(pos + 1, high)

        quick_sort(0, len(nums) - 1)

        return nums
# example-[t,2,3,1]
# output-[1,2,3,5]
        