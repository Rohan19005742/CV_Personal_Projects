data = [0,2,5,3,8,6,4,7,1,9,5,3,2,8,6,4,0,7,1,9]

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        arr.extend([i] * count[i])
    
    return arr


if __name__ == "__main__":
    sorted_data = counting_sort(data)
    print("Sorted Data:", sorted_data)
    assert sorted_data == sorted(data)
