start_costs = 5.00 #you can change this number to the start price of the ride
costs = 1.30 #you can change this number to the price that you have to pay per Kilometer
km = int(input("How much Kilometers"))
c_costs = start_costs + costs * km
#You can Remove the "if km > 40:" but if you want it change it or keep it like this
if km > 40:
    costs = 1.0
else:
    costs = 1.30

print(f"You have to pay for {km} Kilometers {c_costs} Dollars.")
