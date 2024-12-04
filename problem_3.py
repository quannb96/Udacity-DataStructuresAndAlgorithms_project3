def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    while left and right:
        if left[0] > right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))

    sorted_arr.extend(left)
    sorted_arr.extend(right)
    return sorted_arr

def rearrange_digits(input_list):
    """
    Rearranges the elements of the given array to form two numbers such that their sum is maximized.
    The numbers formed have a number of digits differing by no more than one.
    
    Args:
        input_list (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing two integers
    """
    if not input_list:
        return (0, 0)

    sorted_list = merge_sort(input_list)
    num1, num2 = "", ""

    for i in range(len(sorted_list)):
        if i % 2 == 0:
            num1 += str(sorted_list[i])
        else:
            num2 += str(sorted_list[i])

    return (int(num1), int(num2))

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
