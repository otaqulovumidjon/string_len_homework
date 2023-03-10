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
    a = ''
    if len(s1) % 2 == 1:
        a = s1
    if len(s2) % 2 == 1:
        if len(a)!=0:
            a += ', ' + s2
        else:
            a = s2
    if len(s3) % 2 == 1:
        if len(a)!=0:
            a+= ', ' + s3
        else:
            a = s3
        
    return f'[{a}]'
print(main( s1="code", s2="python", s3="coder"))