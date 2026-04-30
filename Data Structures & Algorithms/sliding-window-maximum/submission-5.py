class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for s in range(k):
            while q and nums[s] > q[-1]:
                q.pop()
            q.append(nums[s])
        res = []
        res.append(q[0])
        l = 0
        for r in range(s + 1, len(nums)):
            print(q)
            while q and nums[r] > q[-1]:
                q.pop()
            q.append(nums[r])
            if nums[l] == q[0]:
                q.popleft()
            l += 1
            res.append(q[0])
            print(q,r)
        return res


        