# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        s = data[index]
        index += 1
        int1 = s[0]
        int2 = s[2]
        if int1 > int2:
            sys.stdout.write(str(int1) + ">" + str(int2) + "\n")
        elif int1 < int2:
            sys.stdout.write(str(int1) + "<" + str(int2) + "\n")
        else:
            sys.stdout.write(str(int1) + "=" + str(int2) + "\n")


if __name__ == "__main__":
#     test_input = """5
# 3<7
# 3>7
# 8=9
# 0=0
# 5<3

#     """
#     sys.stdin = StringIO(test_input)
    main()