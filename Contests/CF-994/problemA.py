# from io import StringIO
import sys

def all_nonzero_subsequences(arr):
    subsequences = []

    current_subsequence = []
    for num in arr:
        if num != 0:
            current_subsequence.append(num)
        else:
            if current_subsequence:
                subsequences.append(current_subsequence)
            current_subsequence = []

    if current_subsequence:
        subsequences.append(current_subsequence)

    return subsequences


def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for i in range(t):
        n = int(data[index])
        index += 1
        numbers = list(map(int, data[index].split()))
        index += 1
        result = 0
        subSequenceCounter = len(all_nonzero_subsequences(numbers))

        if sum(numbers) == 0:
            result = 0
        elif min(numbers) > 0:
            result = 1
        elif subSequenceCounter == 1:
            result = 1
        elif subSequenceCounter > 1:
            result = 2
            
        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
#     test_input = """10
# 4
# 0 1 2 3
# 6
# 0 0 0 0 0 0
# 5
# 1 0 1 0 1
# 5
# 3 1 4 1 5
# 4
# 3 2 1 0
# 7
# 9 100 0 89 12 2 3
# 4
# 0 3 9 0
# 7
# 0 7 0 2 0 7 0
# 1
# 0
# 2
# 0 1

#     """
#     sys.stdin = StringIO(test_input)
    main()