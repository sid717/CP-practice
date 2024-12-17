# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n = int(data[index])
        index += 1
        numbers = list(map(int, data[index].split()))
        index += 1
        # numbers.sort(reverse=True)

        # if n > 2:
        #     while n > 2:
        #         numbers.append(((numbers[n-1] + numbers[n-2])//2))
        #         numbers.pop(n-2)
        #         numbers.pop(n-2)
        #         numbers.sort(reverse=True)
        #         n -= 1

        numbers.sort()
        if n > 2:
            final = ((numbers[0] + numbers[1])//2)
            for i in range(2, n):
                final += numbers[i]
                final //= 2
        else:
            final = sum(numbers) // 2

        sys.stdout.write(str(final) + "\n")
        # sys.stdout.write(str((sum(numbers))//2) + "\n")

if __name__ == "__main__":
#     test_input = """4
# 5
# 1 7 8 4 5
# 3
# 2 6 5
# 5
# 5 5 5 5 5
# 2
# 1 1

#     """
#     sys.stdin = StringIO(test_input)
    main()