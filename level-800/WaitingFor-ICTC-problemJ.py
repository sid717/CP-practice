# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    people, seats = 0, 0

    for _ in range(t):
        char, num = data[index].split()[0], int(data[index].split()[1])
        index += 1

        if char == 'P':
            people += num
        else:
            seats = num
            minimum = min(seats, people)
            seats -= minimum
            people -= minimum
            if seats >= 1:
                sys.stdout.write("YES" + "\n")
            else:
                sys.stdout.write("NO" + "\n")

if __name__ == "__main__":
#     test_input = """10
# P 2
# P 5
# B 8
# P 14
# B 5
# B 9
# B 3
# P 2
# B 1
# B 2

#     """
#     sys.stdin = StringIO(test_input)
    main()