# Problem B: Find how many numbers between a and b are divisible by k

def find_divisible(a, b, k):
    if k == 0:
        return 0  # avoid division by zero
    # Explanation:
    # (b // k) counts how many numbers up to b are divisible by k
    # ((a - 1) // k) counts how many numbers before a are divisible by k
    # Subtracting gives how many numbers between a and b (inclusive) are divisible by k
    return (b // k) - ((a - 1) // k)


# Problem C: Rotate an array A to the right k times

def rotate(A, k):
    if not A:
        return []  # if the list is empty, return empty list
    k = k % len(A)  # if k is bigger than list length, use remainder only
    # A[-k:] takes last k elements, A[:-k] takes everything before that
    # Joining them moves the last k elements to the front, rotating the list
    return A[-k:] + A[:-k]


# Sample usage:
if __name__ == "__main__":
    # Test find_divisible
    print("find_divisible(6, 11, 2) =", find_divisible(6, 11, 2))  # Output: 3
    print("find_divisible(0, 11, 2) =", find_divisible(0, 11, 2))  # Output: 6

    # Test rotate
    print("rotate([3, 8, 9, 7, 6], 3) =", rotate([3, 8, 9, 7, 6], 3))  # Output: [9, 7, 6, 3, 8]
    print("rotate([0, 0, 0], 1) =", rotate([0, 0, 0], 1))              # Output: [0, 0, 0]
    print("rotate([1, 2, 3, 4], 4) =", rotate([1, 2, 3, 4], 4))        # Output: [1, 2, 3, 4]
