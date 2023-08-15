import numpy as np
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
        self.estimated_net_profit = self.avg_units*(self.avg_price- self.estimated_cost) - self.fixedCosts

    def calError(self, true_price):
        self.true_price = true_price
        self.error = abs(self.estimated_net_profit-self.true_price)/self.true_price

    def get_sales_volume_price(self, ):
        self.market_scenario = [self.slow, self.normal, self.hot]
        scenario = self.market_scenario[np.random.choice([0,1,2])] # random choice as per uniform distribution
        return scenario
    
    def simulation(self, iters ):
        avg_net_profit = 0
        for i in range(iters):
            scenario = self.get_sales_volume_price()
            avg_net_profit += ((scenario[0]*(scenario[1]-self.estimated_cost) - self.fixedCosts)/iters)
        return avg_net_profit





slow = [50000, 11.00]
normal = [75000, 10.00]
hot = [100000, 8.00]
monte_carlo = MonteCarlo(slow, normal, hot, 120000)
monte_carlo.calNetProfit(6.50)
monte_carlo.calError(93000)
scenario = monte_carlo.get_sales_volume_price()

print("Average price: $", monte_carlo.avg_price)
print("Average number of units sold: ", monte_carlo.avg_units)
print("Net profit: $", monte_carlo.estimated_net_profit)
print("Error in Estimate: ", monte_carlo.error *100, "%")
print("Avg net profit as per monte carlo simulations: $", monte_carlo.simulation(100000))




