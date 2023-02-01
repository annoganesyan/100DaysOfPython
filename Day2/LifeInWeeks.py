age = input("What is your current age? ")

days = int(age)*365
weeks = int(age)*52
months = int(age)*12

days_left = 90 * 365 - days
weeks_left = 90 * 52 - weeks
months_left = 90 * 12 - months

print("You have "+ str(days_left) + " days, " + str(weeks_left) + " weeks, and " + str(months_left) + " months left.")
