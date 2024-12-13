from io import StringIO
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
 
        # maxIndex = array.index(max(array))
        # maxNum = max(array) 
        i = 0
        colored1 = []
        colored2 = []
        
        if n % 2 == 0:
            score = max(array) + (n//2)
        else:        
            array.append(0)
            for j in range(0, n, 2):
                colored2.append(array[j])

            while i < n:
                if array[i] >= array[i+1]:
                    colored1.append(array[i])
                    i += 2
                elif array[i] < array[i+1]:
                    colored1.append(array[i+1])
                    i += 3
            score = max(max(colored1) + len(colored1), max(colored2) + len(colored2))
 
        sys.stdout.write(str(score) + "\n")
 
if __name__ == "__main__":
    test_input = """4
3
5 4 5
3
4 5 4
10
3 3 3 3 4 1 2 3 4 5
9
17 89 92 42 29 92 14 70 45
 
    """
    sys.stdin = StringIO(test_input)
    main()