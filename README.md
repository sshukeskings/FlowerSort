# FlowerSort
# Flower Sort Algorithm

The Flower Sort algorithm is a fictional sorting algorithm inspired by the merge sort algorithm. It follows a divide-and-conquer approach to efficiently sort a list of numbers.

## Algorithm Description

The Flower Sort algorithm works as follows:

1. **Divide:** The input list is divided into two halves recursively until the base case is reached. The base case is when the list has one or zero elements, which are considered sorted.

2. **Sort:** The left and right halves are sorted using the Flower Sort algorithm recursively.

3. **Merge:** The sorted sublists are merged back together by comparing elements from each sublist and adding them to a new merged list in the correct order.

The algorithm continues dividing, sorting, and merging until the entire list is sorted.

## Performance Analysis:

The "Flower Sort" algorithm has a time complexity of O(n log n) on average and in the worst case, similar to merge sort. This makes it an efficient algorithm for sorting large input sizes.

As for comparisons with other well-known sorting algorithms, the "Flower Sort" algorithm shares similarities with merge sort in terms of its divide-and-conquer approach and time complexity. However, it differs in terms of naming and potentially in implementation details, which could affect factors such as space complexity and performance optimizations.

## Implementation

The provided implementation is in Python.

### Requirements

- Python 3.x

### Usage

1. Import the `flower_sort` function into your Python program or script.

2. Call the `flower_sort` function, passing the list of numbers as the argument.

3. The function will return a new list with the numbers sorted in ascending order.

```python
from flower_sort import flower_sort

numbers = [4, 2, 7, 1, 3]
sorted_numbers = flower_sort(numbers)

print(sorted_numbers)

