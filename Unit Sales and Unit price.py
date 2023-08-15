# Calculate the average units and the unit price that you expect to sell,
# which depend on the market state. Use the assumptions above to compute
# the expected quantity of products and their expected unit price.
import numpy

# In a "slow" market, you expect to sell 50,000 units at an average selling price of $11.00 per unit
# In a "normal" market, you expect to sell 75,000 units, but you'll likely realize a lower average selling price of $10.00 per unit
# In a "hot" market, you expect to sell 100,000 units, but this will bring in competitors, who will drive down the average selling price to $8.00 per unit

slow = [50000, 11.00]
normal = [75000, 10.00]
hot = [100000, 8.00]

avg_price = (slow[1] + normal[1] + hot[1])/3 # all are equally likely
avg_units = (slow[0]+normal[0]+hot[0])/3

print("Average price: ", avg_price)
print("Average number of units sold: ", avg_units)