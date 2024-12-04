def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None  # Square root is not defined for negative numbers
    if number == 0 or number == 1:
        return number

    start, end = 0, number
    while start <= end:
        mid = (start + end) // 2
        mid_squared = mid * mid

        if mid_squared == number:
            return mid
        elif mid_squared < number:
            start = mid + 1
            floor_sqrt = mid
        else:
            end = mid - 1

    return floor_sqrt

# Test cases
print("Pass" if 3 == sqrt(9) else "Fail")
print("Pass" if 0 == sqrt(0) else "Fail")
print("Pass" if 4 == sqrt(16) else "Fail")
print("Pass" if 1 == sqrt(1) else "Fail")
print("Pass" if 5 == sqrt(27) else "Fail")