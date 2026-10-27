
# A function that returns the largest of its three parameters, which are real numbers.

def largest(num1: float, num2: float, num3: float):
    return  max(num1, num2, num3)
    
try:
    largest_num = largest('a', 2, 3)
    print(f"Largest number is {largest_num}")

except TypeError:
    print("Invalid Attributes. Please enter 3 valid decimal attributes")

except KeyboardInterrupt:
    print("Program interrupted in the middle of execution")