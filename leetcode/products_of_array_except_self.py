import timeit
import math

# brute force, phương pháp nông dân, O(n^2)
# tạo list copy và xóa phần tử i
# tính tích các phần tử còn lại
# nhưng vì math.prod là O(n), thêm for loop cũng O(n) => O(n^2)
def productExceptSelf(nums: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            res.append(int(math.prod(temp)))
        return res


# ============================


# division method, tốt hơn ở trên vì O(n)
# chia ra các trường hợp:
# - không có số 0: tính tích tất cả các phần tử, sau đó chia
# - có số 0: chỉ cần tính tích các phần tử còn lại, gán index số 0
# - có nhiều hơn 1 số 0: tất cả các phần tử đều là 0
def productExceptSelf2(nums: list[int]) -> list[int]:
        zero = nums.count(0)
        if zero == 0:
            prod = math.prod(nums)
            return [prod // x for x in nums]
        elif zero == 1:
            prod = math.prod(x for x in nums if x != 0)
            res = [0] * len(nums)
            res[nums.index(0)] = prod
            return res
        else:
            res = [0] * len(nums)
        return res

nums = [i % 21 - 10 for i in range(1000)]

print('cach 1: ', timeit.timeit(lambda: productExceptSelf(nums), number=10))
print('cach 2: ', timeit.timeit(lambda: productExceptSelf2(nums), number=10))
# cach 1:  0.1070278999995935
# cach 2:  0.0005201000003580702