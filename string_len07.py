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
    l1 = (len(s1)+1) % 2
    l2 = (len(s2)+1) % 2
    l3 = (len(s3)+1) % 2
    
    if l1 == 1 and l2 == 1:
        odd = s1 , s2
    if l1 == 1 and l3 == 1:
        odd = s1 , s3
    if l2 == 1 and l3 == 1:
        odd = s2 , s3
    if l1 == 1 and l2 == 1 and l3 == 1:
        odd = s1 , s2 , s3
    return [odd]
print(main("long" , "middle of the night", "sign"))