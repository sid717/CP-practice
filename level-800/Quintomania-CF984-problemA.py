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
        notes = list(map(int, data[index].split())) 
        index += 1
        isPerfect = True

        for i in range(n-1):
            if abs(notes[i]-notes[i+1]) == 5 or abs(notes[i]-notes[i+1]) == 7:
                continue
            else:
                isPerfect = False
                break

        if isPerfect == False:
            sys.stdout.write("NO" + "\n")
        else:
            sys.stdout.write("YES" + "\n")


if __name__ == "__main__":
#     test_input = """8
# 2
# 114 109
# 2
# 17 10
# 3
# 76 83 88
# 8
# 38 45 38 80 85 92 99 106
# 5
# 63 58 65 58 65
# 8
# 117 124 48 53 48 43 54 49
# 5
# 95 102 107 114 121
# 10
# 72 77 82 75 70 75 68 75 68 75
 
#     """
#     sys.stdin = StringIO(test_input)
    main()