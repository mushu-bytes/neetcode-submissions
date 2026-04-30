class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed), key=lambda x: x[0])
        stack = []
        while cars:
            car = cars.pop()
            rate = (target - car[0]) / car[1]
            if not stack or rate > stack[-1]:
                stack.append(rate)
        return len(stack)


