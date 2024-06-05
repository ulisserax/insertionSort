#insertion_sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

# Test
print(insertion_sort([2, 22, 15, 7, 9, 14, 10, 3, 69, 90, 12])) # [2, 3, 7, 9, 10, 12, 14, 15, 22, 69, 90]