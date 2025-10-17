data = [0,2,5,3,8,6,4,7,1,9,5,3,2,8,6,4,0,7,1,9]

def counting_sort(arr):
    count = [0] * 10
    sorted_data = []
    for num in arr:
        count[num] += 1

    for i in range(len(count)):
        sorted_data.extend([i] * count[i])
    
    return sorted_data


if __name__ == "__main__":
    sorted_data = counting_sort(data)
    print("Sorted Data:", sorted_data)
    assert sorted_data == sorted(data)
