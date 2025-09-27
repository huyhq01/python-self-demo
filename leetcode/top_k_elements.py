from typing import List, DefaultDict

# dùng bucket sort 
def topKFrequent(nums: List[int], k: int):
    count = DefaultDict(int) # nếu key chưa có value mặc định = 0, đúng hơn là falsy value
    buckets = [[] for _ in range(len(nums) + 1)]
    # [[], [], [], [], [], [], []] mỗi [] là 1 bucket
    # số bucket xấu nhất = max len(nums) vì mỗi số sẽ khác nhau

    for num in nums:
        count[num] += 1
    # 'count' tần số xuất hiện của mỗi số <=> {num: (freq)+=1}

    for num, freq in count.items():
        buckets[freq].append(num)
    # 'buckets' nhóm các số có cùng tần số xuất hiện vào cùng 1 bucket
    # vì sao lại không dùng num làm index?
    # vì num có thể âm, hoặc rất lớn

    # duyệt ngược các bucket từ cao đến thấp
    # lấy k số xuất hiện trong các bucket
    result = []
    for i in reversed(range(len(buckets))):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result


# print(topKFrequent([1, 1, 1, 3, 2, 3], 2))