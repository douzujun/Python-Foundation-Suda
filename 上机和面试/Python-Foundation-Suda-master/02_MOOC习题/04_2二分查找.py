import random

def binary_search(L, t, low, high):
    while low <= high:
        mid = (low + high) // 2
        if L[mid] == t:
            return True
        elif L[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    return False


if __name__ == "__main__":
    L = [random.randint(0,30) for _ in range(20)]
    L.sort()

    print(L)
    print(binary_search(L, 14, 0, len(L)-1))