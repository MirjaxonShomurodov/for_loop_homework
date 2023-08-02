def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    b=[]
    a=2.25
    for i in range(1,price):
        b.append(i*a)
    return list(b)
print(main(price=10))