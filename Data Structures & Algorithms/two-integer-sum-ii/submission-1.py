class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # if no extra space, its probably a two pointer type solution
        # indices are 1 indexed and have to add up to target
        # numbers are non-decreasing. 
        
        # key elements are the fact that the array is non decreasing

        l, r = 0, len(numbers) - 1
        while l < r:
            curr = numbers[l] + numbers[r]
            if curr < target:
                l += 1
            elif curr > target:
                r -= 1
            else:
                return [l + 1, r + 1]