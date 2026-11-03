
def sort_array(A, n):
    if not isinstance(A, list) or not isinstance(n, int):
        raise TypeError("Invalid input")

    if not all(type(x) == int for x in A[:n]):
        raise TypeError("Invalid input")

    A[:n] = sorted(A[:n])
    return A


try:
    A = [5, 2, 8, 1, 3]
    n = 5

    sorted_array = sort_array(A, n)
    print(f"The sorted array is: {sorted_array}")

except TypeError:
    print("Invalid Attributes. Please enter valid attribute")

except KeyboardInterrupt:
    print("Program interrupted in the middle of execution")


