price_per_apple = 25 # in pence
price_per_banana = 50 # in pence 

num_apples = int(input("How many apples do you want to buy? "))
num_bananas = int(input("how many bananas do you want to buy? "))

total_cost_apples = num_apples * price_per_apple
total_cost_bananas = num_bananas * price_per_banana
total_cost_of_both = total_cost_apples + total_cost_bananas

print(f"The total cost of {num_apples} apples is {total_cost_apples}.")
print(f"The total cost of {num_bananas} apples is {total_cost_bananas}.")
print(f"The total cost of both combines is {total_cost_of_both}. ")