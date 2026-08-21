import sys
from fractions import Fraction
from decimal import Decimal # decimal exist in python.
ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp: { ideal_temp}")
print(f"current temp: { current_temp}")
print(f"Difference temp: { ideal_temp - current_temp}")
print(sys.float_info)