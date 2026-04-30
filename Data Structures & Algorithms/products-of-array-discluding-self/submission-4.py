class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # goal: return a list output, where each element, output[i]
        # is the product of all elements in nums, except i
        # immediate thought: in order to do this fast, we need to somehow know
        """
        the product of the rest of the list. or we need to be able to deduce it in 
        constant time.
        What would be brute force? The brute force solution would be to spend n squared
        time looping through nums, calculating the product of ther est of the list
        Lots of redundancy because we are constantly calculating portions of the list
        that has already been calculated before. 
        As a result, we can use presums and post sums to precalculate everything
        Define presums: List[int] where presums[i] is the product of the array before i, excluding nums[i]
        Define postsums: List[int] where postsums[i] is the prpduct of the array after i, excluding nums[i]
        """
        preSum = 1
        preSums = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            preSum *= nums[i - 1]
            preSums[i] = preSum

        postSum = 1
        postSums = [1 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            postSum *= nums[i + 1]
            postSums[i] = postSum

        res = []
        for i in range(len(nums)):
            res.append(postSums[i] * preSums[i])

        return res