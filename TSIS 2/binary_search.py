def binary_search(a: list[int], left: int, right: int, n: int) -> int:
    mid = (left + right) // 2

    if left > right:
        return -1
    
    if n == a[mid]:
        return mid
    
    if n > a[mid]:
        return binary_search(a, mid + 1, right, n)
    if n < a[mid]:
        return binary_search(a, left, mid - 1, n)


a = [6, 12, 14, 18, 22, 39, 55, 182]
n = len(a)
low = 0
high = n - 1

key = 22
print(binary_search(a, low, high, key))

key = 54
print(binary_search(a, low, high, key))