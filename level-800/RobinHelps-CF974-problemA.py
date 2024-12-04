# from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, k = map(int, data[index].split())
        index += 1
        people = list(map(int, data[index].split()))
        index += 1
        
        robinGold = 0
        peoplewithGold = 0

        for i in range(n):
            if people[i] >= k:
                robinGold += people[i]
            elif people[i] == 0 and robinGold > 0:       
                robinGold -= 1
                peoplewithGold += 1           

        sys.stdout.write(str(peoplewithGold) + "\n")


if __name__ == "__main__":
#     test_input = """4
# 2 2
# 2 0
# 3 2
# 3 0 0
# 6 2
# 0 3 0 0 0 0
# 2 5
# 5 4

#     """
#     sys.stdin = StringIO(test_input)
    main()