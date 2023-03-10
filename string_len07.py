def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    if len(s1)%2==1:
        x1 = s1
    else:
        return
    if len(s2)%2==1:
        x2 = s2
    else:
        return
    if len(s3)%2==1:
        x3 = s3
    else:
        return
    return f"""[{x1}, {x2}, {x3}]"""

print(main("hello", "computer", "string"))