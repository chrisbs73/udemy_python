# constants
cost_per_hr = 0.51
cost_per_day = cost_per_hr * 24
operation_fund = 918

days_in_month = input('How may days in the month? ')
month_cost = cost_per_day * int(days_in_month)

print('Cost to run 1 server for a day is ${}'.format(cost_per_day))
print('Cost to run 1 server over {} in a month is ${}'.format(days_in_month, month_cost))
print('Cost to run 20 servers for a day is ${0:.2f}'.format(cost_per_day*20))
print('Cost to run 20 servers over {0} in a month is ${1:.2f}'.format(days_in_month, month_cost*20))
print('With an operation fund of {} we can run 1 server for {} days.'.format(operation_fund,int(operation_fund/cost_per_day)))
