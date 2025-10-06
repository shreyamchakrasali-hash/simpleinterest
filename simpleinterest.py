# Simple and Compound Interest Calculator

# Input values
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time (in years): "))

# Calculate Simple Interest
SI = (P * R * T) / 100
print("Simple Interest: ₹", round(SI, 2))
# Calculate Compound Interest
A = P * (1 + R / 100) ** T
CI = A - P
print("Compound Interest: ₹", round(CI, 2))
