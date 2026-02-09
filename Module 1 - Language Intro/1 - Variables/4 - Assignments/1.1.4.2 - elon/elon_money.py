"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###
P = 33000000000 #Principal is the same for both options

# Establishing variables for 10 year option
r = 3.96/100      #interest rate for the 10-year option
n = 10            #period of 10 years

#Establishing the variables for 20 year option
R = 4.32/100      # interest rate for the 20-year option
N = 20            # period of 20 years

# final answer for 10-year
ten_year_final = P*((1+r)**n)
print(ten_year_final)

# final answer for 20-year
twenty_year_final = P*((1+R)**N)
print(twenty_year_final)
