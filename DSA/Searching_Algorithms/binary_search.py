'''
This is an implementation of binary search algorithm in python
'''

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left != right:
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        elif mid < target:
            left = mid + 1
        else:
            right = mid + 1
    return -1


if __name__ == "__main__":
    target = 7
    result = binary_search(data, target)
    print(f"Element {target} found at index: {result}")
    assert result == data.index(target)