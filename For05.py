def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    a=range(B,A,-1)
    return list(a)
print(main(B=10,A=1))