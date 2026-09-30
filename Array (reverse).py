if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    result = arr[::-1]

    print(*result)
