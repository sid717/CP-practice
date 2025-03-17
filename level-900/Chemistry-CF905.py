# from io import StringIO
import sys

def count_characters(s):
    char_count = {}
    for char in s: 
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, k = map(int, data[index].split())
        index += 1
        s = data[index]
        index += 1

        palin = False
        if len(set(s)) == 1:
            palin = True
        elif n - k <= 1:
            palin = True
        else:
            char_count = count_characters(s)

            # odd_numbers = {key: value for key, value in char_count.items() if value % 2 != 0}
            odd = sum(map(lambda x: x % 2, char_count.values()))
            # even_numbers = {key: value for key, value in char_count.items() if value % 2 == 0}

            if odd-1 == k or odd <= k:
                palin = True
            # sorted_even_numbers = dict(sorted(even_numbers.items(), key=lambda x: x[1]))

            # items = {**sorted_odd_numbers, **sorted_even_numbers}
            # for item in items:
            #     if k > 0:
            #         subtract = min(k, items[item])
            #         items[item] -= subtract
            #         k -= subtract
            # items = {k: v for k, v in items.items() if v != 0}            
            # for item in items:
            #     value = items[item]
            #     if value & 1 == 0:
            #         even += 1
            #     else:
            #         odd += 1

            # if odd <= 1 and even >= 0:
            #     palin = True

        # print("YES" if palin else "NO")

        print("YES" if palin else "NO")

if __name__ == "__main__":
#     test_input = """14
# 1 0
# a
# 2 0
# ab
# 2 1
# ba
# 3 1
# abb
# 3 2
# abc
# 6 2
# bacacd
# 6 2
# fagbza
# 6 2
# zwaafa
# 7 2
# taagaak
# 14 3
# ttrraakkttoorr
# 5 3
# debdb
# 5 4
# ecadc
# 5 3
# debca
# 5 3
# abaac

#     """
#     sys.stdin = StringIO(test_input)
    main()