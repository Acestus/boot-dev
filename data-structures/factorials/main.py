def num_possible_orders(num_posts):
    product = 1
    for i in range(2, num_posts + 1):
        product *= i
    print(f"Number of possible orders for {num_posts} posts: {product}")
    return product

num_possible_orders(4)