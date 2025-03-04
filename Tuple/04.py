# Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.

foods = [("Burger", 5), ("Pizza", 10), ("Pasta", 7)]
foods.sort(key=lambda x: x[1], reverse=True)
print(foods)
