class MonteCarlo():
    def __init__(self, slow, normal, hot, fixedCosts) -> None:
        self.slow = slow
        self.normal = normal
        self.hot = hot
        self.fixedCosts = fixedCosts
        self.avg_price = 0
        self.avg_units = 0

    def avgSellingPrice_avg_units(self):
        self.avg_price = (self.slow[1] + self.normal[1] + self.hot[1])/3 # all are equally likely
        self.avg_units = (self.slow[0] + self.normal[0] + self.hot[0])/3

    def calNetProfit(self, estimated_cost ):
        self.avgSellingPrice_avg_units() # init variables
        self.estimated_cost = estimated_cost
        self.net_profit = self.avg_units*(self.avg_price- self.estimated_cost) - self.fixedCosts




slow = [50000, 11.00]
normal = [75000, 10.00]
hot = [100000, 8.00]
monte_carlo = MonteCarlo(slow, normal, hot, 120000)
monte_carlo.calNetProfit(6.50)
print("Average price: ", monte_carlo.avg_price)
print("Average number of units sold: ", monte_carlo.avg_units)
print("Net profit: ", monte_carlo.net_profit)




