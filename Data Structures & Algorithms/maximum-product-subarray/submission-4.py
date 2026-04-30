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
        prod = 1
        absolute = 1
        negatives = 0
        for num in nums:
            prod = max(num, num * prod)
            maxProd = max(prod, maxProd)
            absolute *= num
            if num < 0: negatives += 1
            if negatives > 0 and negatives % 2 == 0:
                maxProd = max(absolute, maxProd)
        return maxProd

