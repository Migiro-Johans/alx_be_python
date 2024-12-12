def cal(principal, rate, time):
    interest = principal * rate * time
    return interest

principal = 1000
rate = 0.05
time = 3 

interest = cal(1000, 0.05, 3)
print(f"The simple interest is: {interest}")
