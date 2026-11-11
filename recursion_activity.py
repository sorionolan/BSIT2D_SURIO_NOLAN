def sum_array(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_array(arr[1:])


def find_largest(arr):
    if len(arr) == 1:
        return arr[0]

    largest_rest = find_largest(arr[1:])

    if arr[0] > largest_rest:
        return arr[0]
    else:
        return largest_rest


def count_number(arr, target):
    if len(arr) == 0:
        return 0

    if arr[0] == target:
        return 1 + count_number(arr[1:], target)
    else:
        return count_number(arr[1:], target)


print("1. SUM THE ARRAY")
print(sum_array([]))
print(sum_array([5]))
print(sum_array([1, 2, 3, 4]))
print(sum_array([-2, 5, -3, 4]))

print("\n2. FIND THE LARGEST NUMBER")
print(find_largest([5]))
print(find_largest([10, 5, 8, 20, 3]))
print(find_largest([2, 9, 4, 15, 7]))
print(find_largest([-5, -2, -10, -1]))

print("\n3. COUNT A CHOSEN NUMBER")
print(count_number([], 5))
print(count_number([2, 5, 5, 3, 5, 1], 5))
print(count_number([1, 2, 3, 4], 7))
print(count_number([4, 4, 4, 4], 4))


