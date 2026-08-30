def recommend_product(products):
    """
    Recommend the most suitable product.
    """

    if not products:
        return None

    products = sorted(products, key=lambda x: x["price"])

    return products[0]
