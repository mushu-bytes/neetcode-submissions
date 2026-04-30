class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Goal: return the number of different car fleets
        A car fleet is a non-empty set of cars driving at the same position and speed

        If a car catches up to a car fleet, then the car is apart of the fleet.
        So we have target, position and speed
        I think I definitely need to leverage the property that only if a car catches up to a speed

        What is brute force? For each car, check the rest of the array
        for whether there is a car fleet it will join, and keep track
        of the different car fleets

        What is the flaw here: we are repeatedly checking cars that
        probably won't be caught

        I think position might be the biggest limiting factor. If 
        you are positioned behind car, you either become the car fleet
        or not

        Can we keep a monotonically decreasing stack of each car (pos, speed),
        and we can check whether each car will its own car fleet

        Problem: the cars are not sorted by position.
        """
        # turn = math.ceil(target - position // speed)
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)






