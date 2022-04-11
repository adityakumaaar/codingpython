## Tips to work with arrays and revision points

<br>

- Arrays in python are implemented through list.

<br>

- Common array functions are len(A), A.append(val), A.remove(val), A.insert(pos, val).

<br>

- Checking if value is present in list by using 'in' operator

<br>

- Copies in arrays are made using 'copy' module. There is difference between deepcopy and shallowcopy (copy). B= A[:] does a shallow copy. More information, [GFG](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/), [Blog](https://www.sololearn.com/Discuss/1953558/python-what-is-the-difference-between-those-statements).

<br>

- Bisect module is used to find the position of a new element in already sorted list so that the list remains sorted
  - bisect.bisect(list, num)
  - bisect.bisect_left(list, num) -> will return the left position if 'num' already present in list
  - bisect.bisect_right(list, num) -> will return the right position if 'num' already present in list

<br>

- Slicing : A = [1,6,3,4,5,2,7]
  - A[2:4] = [3,4] -> last element is not taken
  - A[2:] = [3,4,5,2,7]
  - A[:4] = [1,6,3,4] -> last position is not taken
  - A[:-1] = [1,6,3,4,5,2] -> everything except last
  - A[-3:] = [5,2,7] -> start counting from right end with -1
  - A[-3:-1] = [5,2]
  - A[1:5:2] = [6,4] -> last index denotes skip
  - A[5:1:-2] = [2,4] -> with negative skip, start index > end index
  - Reverse a list : A[::-1]
  - Rotate a list by k to left : A[k:] + A[:k]

<br>

- List comprehension consists of
  - Input Sequence
  - Iterator over the input sequence
  - Logical condition over the iterator (optional)
  - Expression that yields the elements of the derieved list
    - [x**2 for x in range(6)] = [0, 1, 4, 9, 16, 25]
    - [x**2 for x in range(6) if x%2 == 0] = [0, 4, 16]
