import heapq

num = [5, 3, 8, 1, 2, 7, 4, 6, 9]
heapq.heapify(num)
# print(num) -> [1, 2, 4, 3, 5, 7, 8, 6, 9], vì sao?
# đây là một list bình thường, không phải đã sắp xếp
# đồng thời là một heap, cấu trúc dữ liệu đặc biệt
# để là 1 heap thỏa mãn 2 yêu cầu: node cha luôn nhỏ hơn node con
# và cây luôn được lấp đầy từ trái sang phải
# heapq là một min-heap, phần tử nhỏ nhất luôn ở đầu
# heaify tạo ra một heap từ một list bất kỳ
# cho nên heapq.heapify tạo ra mảng như trên
#               1
#            /     \
#           2       4
#        /   \     / \
#       3     5   7   8
#     /  \  
#    6    9      
#
for i in range(len(num)):
    print(heapq.heappop(num))
# lấy node nhỏ nhất, tức node root = trên cùng -> [1, 2, 3, 4, 5, 6, 7, 8, 9]