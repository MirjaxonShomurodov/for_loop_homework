def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    list = []
    for i in range(k):
        list.append(n)
    return list
print(main(k=3,n=5))