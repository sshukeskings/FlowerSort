def flower_sort(numbers):
    n = len(numbers)
    
    # Base case: If the list has one or zero elements, it is already sorted
    if n <= 1:
        return numbers
    
    # Divide the list into two halves
    mid = n // 2
    left_half = numbers[0:mid]
    right_half = numbers[mid:n]
    
    # Sort the left and right halves using flower sort recursively
    sorted_left = flower_sort(left_half)
    sorted_right = flower_sort(right_half)
    
    # Merge the sorted halves
    merged = merge(sorted_left, sorted_right)
    
    return merged

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    # Compare elements from left and right sublists and add them to the merged list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Add any remaining elements from the left sublist
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    
    # Add any remaining elements from the right sublist
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    
    return merged
