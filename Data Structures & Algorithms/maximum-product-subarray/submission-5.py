class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Since we have to consider all possible sub
        arrays, this is definitely either a backtracking
        or DP problem. Since we are returning an int,
        its definitely a DP

        s[i] is the max prod subarray of the first i elements,
        i <= len(nums)
        s[0] = nums[0]
        max(s) is the solution
        formula:
        i think this is basically the solution to
        the max subarray problem haha, but this
        one is a bit more interesting because of
        how negatives work. I think we may have to 
        consider
        """
        maxProd = nums[0]
        currMin, currMax = 1, 1
        for num in nums:
            tmp = currMax * num
            currMax = max(tmp, currMin * num, num)
            currMin = min(tmp, currMin * num, num)
            maxProd = max(currMax, maxProd)
        return maxProd

