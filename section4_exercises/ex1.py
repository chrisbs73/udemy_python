# per hours cost 0.51 per hour
cost_per_hr = 0.51
print('How munch it costs to run a server.  Server cost is ${} per hour.'.format(cost_per_hr))

# how much does it cost to run for one day
day_cost = cost_per_hr * 24
print('Server cost per day is ${}'.format(day_cost))

# cost per month
days_in_month = input('How may days in the month? ')
month_cost = day_cost * int(days_in_month)
print('For {} days in the month it costs ${} to run the server.'.format(days_in_month, month_cost))