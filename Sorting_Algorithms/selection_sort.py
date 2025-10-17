data = [4,233,66,8,14,4,86,5,7,3,9,0,10,255,23,56,78,12]


def selection_sort(arr):
    for x in range(len(arr)):
        min_value = 9999999999999999
        min_index = -1
        for y in range(x, len(arr)):
            if arr[y] < min_value:
                min_value = arr[y]
                min_index = y
        arr[x], arr[min_index] = arr[min_index], arr[x]
    return arr


if __name__ == "__main__":
    sorted_data = selection_sort(data)
    print("Sorted Data:", sorted_data)
    assert sorted_data == sorted(data)