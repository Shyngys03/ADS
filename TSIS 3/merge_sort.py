def merge_two_list(a: list[int], b: list[int]):
    i = j = 0
    merged_list = []

    while i < len(a) and j < len(b):
        merged_list.append(min(a[i], b[j]))

        i, j = (i + 1, j) if a[i] < b[j] else (i, j + 1)

    if i < len(a):
        merged_list += a[i:]
    if j < len(b):
        merged_list += b[j:]

    return merged_list


def merge_sort(arr: list[int]):
    if len(arr) == 1:
        return arr
    
    medium = len(arr) // 2

    left = merge_sort(arr[medium:])
    right = merge_sort(arr[:medium])

    return merge_two_list(left, right)


if __name__ == "__main__":
    
    a = list(map(int, input().split()))

    print(merge_sort(a))