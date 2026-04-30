class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr = {}
        res = []
        maxWindow = 0
        for s in range(k):
            maxWindow = max(maxWindow, nums[s])
            curr[nums[s]] = 1 + curr.get(nums[s], 0)
        res.append(maxWindow)
        l = 0

        for r in range(s + 1, len(nums)):
            curr[nums[r]] = 1 + curr.get(nums[r], 0)
            maxWindow = max(maxWindow, nums[r])
            curr[nums[l]] -= 1
            if not curr[nums[l]]:
                del curr[nums[l]]
                if maxWindow == nums[l]:
                    maxWindow = max(curr.keys())
            l += 1
            res.append(maxWindow)
        return res


        