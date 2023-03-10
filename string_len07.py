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
    if len(s1)%2==1 and len(s1)>0:
        x1 = s1
    else:
        x1 = ""

    if len(s2)%2==1 and len(s2)>0:
        x2 = ', '+s2
    else:
        x2 = ""

    if len(s3)%2==1 and len(s3)>0:
        x3 = ', '+s3
    else:
        x3 = ""

    return f"[{x1}{x2}{x3}]"

print(main(s1="codeschool.uz", s2="example", s3="python"))