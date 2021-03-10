#!/usr/bin/env python3

from collections import Counter
from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
    counter = Counter(nums)
    nums, triplets = list(counter.keys()), set()
    if counter[0] >= 3:
        triplets.add((0, 0, 0))
    positives, negatives = [n for n in nums if n > 0], [n for n in nums if n < 0]
    for a in negatives:
        for b in positives:
            c = -(a + b)
            if c in counter and ((c != a and c != b) or counter[c] > 1):
                triplets.add(tuple(sorted([a, b, c])))
    return triplets