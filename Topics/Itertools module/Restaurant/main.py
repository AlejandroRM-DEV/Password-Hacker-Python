import itertools

budget = 30

# Generate all possible combinations of dishes using itertools.product()
all_combinations = itertools.product(main_courses, desserts, drinks)
all_prices = itertools.product(price_main_courses, price_desserts, price_drinks)

# Iterate through each combination and check if it fits within the budget
for combination, prices in zip(all_combinations, all_prices):
    main_course, dessert, drink = combination
    main_course_price, dessert_price, drink_price = prices
    total_cost = main_course_price + dessert_price + drink_price
    if total_cost <= budget:
        print(f"{main_course} {dessert} {drink} {total_cost}")
