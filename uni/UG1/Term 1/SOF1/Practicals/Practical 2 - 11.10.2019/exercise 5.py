age = int(input("Enter your age."))
rate = int(input("Enter your current heart rate."))
max_heart_rate = 208 - (0.7*age)

if rate >= (0.9*max_heart_rate):
    training_zone = "interval training."
elif rate >= (0.7*max_heart_rate):
    training_zone = "threshold training."
elif rate >= (0.5*max_heart_rate):
    training_zone = "aerobic training."
else:
    training_zone = "that of a couch potato."

print("According to your age and your current heart rate and our formula, your training zone is", training_zone)
