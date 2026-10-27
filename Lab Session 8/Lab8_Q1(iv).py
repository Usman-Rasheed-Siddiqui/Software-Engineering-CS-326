
def sort_three_integers(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise TypeError("All attributes must be integers.")
    
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return [a, b, c]

try:
    sort_three_integers_list = sort_three_integers('a', 'b', 'c')
    print(f"The sorted list is: {sort_three_integers_list}")

except TypeError as e:
    print(e)

except KeyboardInterrupt:
    print("Program interrupted in the middle of execution")    