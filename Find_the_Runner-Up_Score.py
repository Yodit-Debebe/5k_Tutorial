if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    seen = set(arr)
    sortedArr = sorted(seen)
    print(sortedArr[-2])
