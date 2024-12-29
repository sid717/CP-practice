# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        k = int(data[index])
        index += 1
        numbers = list(map(int, data[index].split()))
        numbers.sort()
        index += 1
        ints = k - 2
        found = False

        # for i in range(k):
        #     for j in range(i+1, k):
        #         if numbers[i] * numbers[j] == ints:
        #                 found = True
        #                 n, m = numbers[i], numbers[j]
        #                 break
        #     if found:
        #         break

        for i in range(k):
            l_b = 0
            u_b = k-1
            while l_b <= u_b:
                mid = (l_b + u_b) // 2
                val_at_mid = numbers[mid]
                if val_at_mid * numbers[i] == ints and i != mid:
                    found = True
                    n, m = numbers[i], val_at_mid
                    break
                elif val_at_mid * numbers[i] > ints:
                    u_b = mid - 1
                else:
                    l_b = mid + 1
            if found:
                break

        sys.stdout.write(str(n) +  " " + str(m)+ "\n")

if __name__ == "__main__":
#     test_input = """5
# 3
# 1 1 2
# 11
# 3 3 4 5 6 7 8 9 9 10 11
# 8
# 8 4 8 3 8 2 8 1
# 6
# 2 1 4 5 3 3
# 8
# 1 2 6 3 8 5 5 3

#     """
#     sys.stdin = StringIO(test_input)
    main()