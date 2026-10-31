# Program to calculate Compound Interest

P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))

A = P * (1 + R / 100) ** T
CI = A - P

print("Total Amount =", A)
print("Compound Interest =", CI)