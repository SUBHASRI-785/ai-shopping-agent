def compare_products(products, budget):
    """
    Compare products based on the user's budget.
    """

    suitable_products = []

    for product in products:
        if product["price"] <= budget:
            suitable_products.append(product)

    return suitable_products
