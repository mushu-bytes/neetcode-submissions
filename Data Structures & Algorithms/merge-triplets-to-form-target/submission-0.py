class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        pivot = []

        for triplet in triplets:
            if self.isValid(triplet, target):
                if not pivot:
                    pivot = triplet
                else:
                    pivot = self.elementWiseMax(pivot, triplet)
        return target == pivot

    def elementWiseMax(self, t1, t2):
        res = []
        for n1, n2 in zip(t1, t2):
            res.append(max(n1, n2))
        return res

    def isValid(self, triplet, target):
        for n1, n2 in zip(triplet, target):
            if n1 > n2:
                return False
        return True