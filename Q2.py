def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] + right_half[j] == target:
                pairs.append((left_half[i], right_half[j]))
                i += 1
                j += 1
            elif left_half[i] + right_half[j] < target:
                i += 1
            else:
                j += 1

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

def find_pairs_with_sum(S, target):
    S.sort()  # Sort the array using Merge Sort
    merge_sort(S)
    
    global pairs
    pairs = []

    for num in S:
        complement = target - num
        if binary_search(S, complement):
            pairs.append((num, complement))

    return pairs

# Example usage:
S = [2, 4, 3, 7, 1, 5, 9, 6]
target = 10
result = find_pairs_with_sum(S, target)
print(result)
