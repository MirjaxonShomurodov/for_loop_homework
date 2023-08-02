def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    a=0
    i=1
    for i in range(1,N):
        a+=(1/(i))
    return a
print(main(N=5))