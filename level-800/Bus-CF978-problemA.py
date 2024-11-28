from io import StringIO
import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        n, r = map(int, data[index].split()) #for individual values
        index += 1
        members = list(map(int, data[index].split())) #for inputting into an array
        index += 1

        for i in range(n):
            if(members[i] % 2 == 1):
                unhappy =+ 1
                members[i] -= 1
            else:
                r = r - members[i]/2


        sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    test_input = """4
3 3
2 3 1
3 3
2 2 2
4 5
1 1 2 2
4 5
3 1 1 3
 
    """
    sys.stdin = StringIO(test_input)
    main()