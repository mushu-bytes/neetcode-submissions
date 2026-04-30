class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # target = num1 + num 2, 0 = num1 + num2 - target
        # screams two sum because we have to care for two indices
        i, j = 0, len(numbers) - 1
        while i <= j:
            curSum = target - (numbers[i] + numbers[j])
            if curSum > 0:
                i += 1
            elif curSum < 0:
                j -= 1
            else:
                return [i + 1, j + 1]
            