# Implement quick sort algorithm

# Partition Function
# 1. Choose a pivot
# 2. Move it to the end of the array
# 3. Take two pointers and swap L and R if L > pivot and R < pivot until L crosses R
# 4. If L is > pivot, swap L with pivot

# Quicksort Function
# 1. Until low<high get partition index
# 2. Do quicksort for left of partition index
# 2. Do quicksort for right of partition index


def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    R = high - 1
    L = low
    while L < R:
        while L < high and arr[L] < pivot:
            L += 1
        while R >= low and arr[R] >= pivot:
            R -= 1
        if L < R:
            arr[L], arr[R] = arr[R], arr[L]
    if arr[L] > pivot:
        arr[L], arr[high] = arr[high], arr[L]
    return L


def quicksort(arr: list, low: int, high: int):
    if low < high:
        partition_index = partition(arr, low, high)
        quicksort(arr, low, partition_index - 1)
        quicksort(arr, partition_index + 1, high)


def main():
    A = [-1, 0, 2, 5, 8, 9, 42, 30, 52]
    quicksort(A, 0, len(A) - 1)
    print(A)


if __name__ == "__main__":
    main()
