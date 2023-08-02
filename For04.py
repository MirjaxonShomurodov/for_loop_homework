def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    a=range(A,B)
    return list(a)
print(main(A=2,B=10))