hrs = input("Enter Hours:")
rt = input("Rate per hour:")

hours_worked = float( hrs )
rate_per_hr = float( rt )
overtime_rate = 1.5 * rate_per_hr

pay_at_normal_rate = 0
pay_at_overtime_rate = 0

if( hours_worked ) > 40:
    pay_at_overtime_rate = (hours_worked - 40) * overtime_rate
    pay_at_normal_rate = 40 * rate_per_hr
else:
    pay_at_normal_rate = hours_worked * rate_per_hr

total_pay = pay_at_overtime_rate + pay_at_normal_rate

print( total_pay )