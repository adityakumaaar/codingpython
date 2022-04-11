# Question 5.1

# Program that taken in the array A and  index i, and rearranges the elements of A such that all the elements less than A[i] (pivot) appear first, followed by elements equal to the pivot, followed by the elements greater than the pivot


def dutch_flag_partition(arr: list, pivot_index: int):
    pivot = arr[pivot_index]
    smaller, equal, larger = 0, 0, len(arr)

    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:  # arr[equal] > pivot
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]


def main():
    arr = [0, 1, 2, 2, 2, 2, 1, 0, 0, 1, 1, 0, 1, 0, 2, 0, 1, 1, 1]
    dutch_flag_partition(arr, 1)
    print(arr)


if __name__ == "__main__":
    main()
