def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    if len(s)==3 and s[0]==s[2]:
        return True
    else:
        return False

print(main("aka"))