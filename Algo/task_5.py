def binary_search(arr, target):
    mid = len(arr)//2
    if target not in arr:
        return -1
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        arr = arr[:mid]
        return binary_search(arr, target)
    if target > arr[mid]:
        arr = arr[mid:]
        return binary_search(arr, target)
print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 6))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 1))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 8))
print(binary_search([], 1))