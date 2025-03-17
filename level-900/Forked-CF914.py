from io import StringIO
import sys

def find_matching_pairs(list1, list2):
    set1 = set(tuple(sublist) for sublist in list1)
    set2 = set(tuple(sublist) for sublist in list2)
    return [(sublist, sublist) for sublist in set1 & set2]

def main():
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    t = int(data[index])
    index += 1

    for _ in range(t):
        a, b = map(int, data[index].split())
        index += 1
        xk, yk = map(int, data[index].split())
        index += 1
        xq, yq = map(int, data[index].split()) 
        index += 1

        if a == b:
            king_calculations = [[xk + a, yk + b], [xk - a, yk - b], [xk + a, yk - b], [xk - a, yk + b]]
            queen_calculations = [[xq + a, yq + b], [xq - a, yq - b], [xq + a, yq - b], [xq - a, yq + b]]
        else:
            king_calculations = [[xk + a, yk + b], [xk - a, yk - b], [xk + a, yk - b], [xk - a, yk + b], [xk + b, yk + a], [xk - b, yk - a], [xk + b, yk - a], [xk - b, yk + a]]
            queen_calculations = [[xq + a, yq + b], [xq - a, yq - b], [xq + a, yq - b], [xq - a, yq + b], [xq + b, yq + a], [xq - b, yq - a], [xq + b, yq - a], [xq - b, yq + a]]
            
        print(len(find_matching_pairs(king_calculations,queen_calculations)))


if __name__ == "__main__":
    test_input = """4
2 1
0 0
3 3
1 1
3 1
1 3
4 4
0 0
8 0
4 2
1 4
3 4

    """
    sys.stdin = StringIO(test_input)
    main()