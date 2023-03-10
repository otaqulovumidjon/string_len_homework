def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    if int(num1)>=0:
        a=num1
    if int(num2)>=0:
        b=num2
    c = int(num1) + int(num2)

    return str(c)

print(main("34", "56"))