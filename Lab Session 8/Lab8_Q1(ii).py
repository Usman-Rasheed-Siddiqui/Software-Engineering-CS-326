
# A function that returns the least common multiple of its two parameters, which must be 
# positive integers. 

def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

def LCM(num1, num2):
    return (num1 * num2) // gcd(num1, num2)

try:
    LCM_num = LCM(-2, -12)
    print(f"LCM of the two numbers is: {LCM_num}")

except TypeError:
    print("Invalid Attributes. Please enter 2 valid integer attributes")

except KeyboardInterrupt:
    print("Program interrupted in the middle of execution")    