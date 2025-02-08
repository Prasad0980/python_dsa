from math import ceil
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    left = 1  # Minimum possible eating speed
    right = max(piles)  # Maximum needed eating speed

    # Binary search for the minimum valid speed
    while left <= right:
        mid = left + (right - left) // 2

        # Calculate total hours needed at this speed
        hours = sum(ceil(pile / mid) for pile in piles)

        # If hours needed is less than or equal to h,
        # try a smaller speed (we want minimum speed)
        if hours <= h:
            right = mid
        else:
            # Speed is too slow, need to try faster
            left = mid + 1

    return left






print(minEatingSpeed([3, 6, 7, 11], 8))
