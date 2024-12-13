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
        array = list(map(int, data[index].split())) 
        index += 1
        result = 0

        if n % 2 == 1:
            array.append(0)
            n += 1

        for i in range(0, n-1, 2):
            result += array[i] - array[i + 1]


        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
#     test_input = """4
# 4
# 1 2 3 17
# 1
# 100
# 2
# 100 100
# 5
# 3 1 4 1 5
   
#     """
#     sys.stdin = StringIO(test_input)
    main()