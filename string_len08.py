def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    if len(s)%2==0:
        x = s[len(s)//2-1:len(s)//2+1]
    else:
        x = s[len(s)//2]
    return x

print(main("123456789"))