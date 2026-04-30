class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {} # {element: count}
        maxFreq = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            maxFreq = max(maxFreq, counts[num])

        freqs = [[] for i in range(len(nums) + 1)] # index: freq. val: [freq elements]
        print(freqs)
        for num, freq in counts.items():
            print(num, freq)
            freqs[freq].append(num)
        
        print(freqs)
        freqElements = []
        countK = k
        for j in range(len(freqs) - 1, -1, -1):
            for e in freqs[j]:
                countK -= 1
                freqElements.append(e)
                if countK == 0:
                    return freqElements