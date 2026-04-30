class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        prev = -1

        for pos, speed in cars:
            if prev == -1:
                fleets += 1
                prev = (target - pos) / speed
                continue
            
            if prev < (target - pos) / speed:
                prev = (target - pos) / speed
                fleets += 1
        return fleets

