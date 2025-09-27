# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

# Constraints:
# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.


import timeit

# mỗi từ sẽ được encode thành: "chiều dài của từ + '#' + từ"
# ví dụ "we" -> "2#we", "say" -> "3#say"
# edit: thay vì dùng "" += thì dùng join sẽ tối ưu hơn
def encode(strs: list[str]) -> str:
    encoded_list = []
    for word in strs:
        encoded_list.append(f"{len(word)}#{word}")
    return ''.join(encoded_list)



def decode(s: str) -> list[str]:
    i = 0
    decoded_list = []
    while i < len(s):
        # tìm ví trí của kí tự '#'
        j = s.find('#', i)

        # chiều dài của từ
        word_length = int(s[i : j])
        
        # ví trí chữ cái đầu tiên của từ, ngay sau dấu #
        start = j + 1

        # vị trí của kí tự cuối cùng của từ + 1 => tìm vị trí độ dài từ tiếp theo
        end = start + word_length

        # lấy từ
        word = s[start:end]

        decoded_list.append(word)
        i = end
        # có thể đưa i lên end cho gọn
    return decoded_list


def solution(list_str):
    print("encode: ", encode(list_str))
    return decode(encode(list_str))


print("decode: ", solution(["we", "say", ":", "yes", "!@#$%^&*()"]))
