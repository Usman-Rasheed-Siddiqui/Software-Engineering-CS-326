
def square_root(num):
    return num ** 0.5

try:
    square_root_num = square_root('-4')
    print(f"The square root is: {square_root_num}")

except TypeError:
    print("Invalid Attributes. Please enter valid attribute")

except KeyboardInterrupt:
    print("Program interrupted in the middle of execution")    