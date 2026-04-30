class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # intuition, all items in nums equal to val must be moved to the back
        # alternatively, all items not equal to val must be moved up front
        nxt = 0
        for i in range(len(nums)):
            if nums[i] != val:
                temp = nums[i]
                nums[i] = val
                nums[nxt] = temp
                nxt += 1
        return nxt


        