# page 19 Program 8.1 Deeply nested if then else statements
# Define constants
YOUNG_DRIVER_AGE_LIMIT = 25
OLDER_DRIVER_AGE = 70
ELDERLY_DRIVER_AGE = 80
YOUNG_DRIVER_PREMIUM_MULTIPLIER = 2
OLDER_DRIVER_PREMIUM_MULTIPLIER = 1.5
ELDERLY_DRIVER_PREMIUM_MULTIPLIER = 2
YOUNG_DRIVER_EXPERIENCE_MULTIPLIER = 2
NO_MULTIPLIER = 1
YOUNG_DRIVER_EXPERIENCE = 2
OLDER_DRIVER_EXPERIENCE = 5

def agecheck(age, experience):
    # Assigns a premium multiplier depending on the age and experience of the driver
    multiplier = NO_MULTIPLIER
    
    if age <= YOUNG_DRIVER_AGE_LIMIT:
        if experience <= YOUNG_DRIVER_EXPERIENCE:
            multiplier = YOUNG_DRIVER_PREMIUM_MULTIPLIER * YOUNG_DRIVER_EXPERIENCE_MULTIPLIER
        else:
            multiplier = YOUNG_DRIVER_PREMIUM_MULTIPLIER
    elif age > OLDER_DRIVER_AGE and age <= ELDERLY_DRIVER_AGE:
        if experience <= OLDER_DRIVER_EXPERIENCE:
            multiplier = OLDER_DRIVER_PREMIUM_MULTIPLIER
        else:
            multiplier = NO_MULTIPLIER
    elif age > ELDERLY_DRIVER_AGE:
        multiplier = ELDERLY_DRIVER_PREMIUM_MULTIPLIER
    
    return multiplier

# Example usage
print(agecheck(22, 1))  # Should print the premium multiplier for a young driver with 1 year of experience
print(agecheck(45, 6))  # Should print the premium multiplier for an older driver with 6 years of experience
print(agecheck(75, 3))  # Should print the premium multiplier for an elderly driver with 3 years of experience
