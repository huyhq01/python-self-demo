from typing import List, DefaultDict


def topKFrequent(nums: List[int], k: int):
    count = DefaultDict(int)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num in nums:
        count[num] += 1

    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for i in reversed(range(len(buckets))):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


# print(topKFrequent([1, 1, 1, 3, 2, 3], 2))