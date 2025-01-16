#!/usr/bin/python3
def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers.

    A peak is an element that is greater than or equal to its neighbors.
    This function uses a binary search approach to find a peak with
    O(log(n)) complexity.

    Args:
        list_of_integers (list): The list of unsorted integers.

    Returns:
        int or None: A peak element from the list,
        or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
