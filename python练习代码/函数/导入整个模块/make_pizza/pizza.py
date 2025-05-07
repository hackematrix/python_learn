def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza")
    for top in toppings:
        print(f"-{top}")
