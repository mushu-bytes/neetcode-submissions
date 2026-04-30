class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        count = 0
        seen = defaultdict(int) # preSum : count
        seen[0] = 1

        for num in nums:
            curSum += num
            if curSum - k in seen:
                count += seen[curSum - k]
            seen[curSum] += 1
            
        return count
