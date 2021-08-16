
# Validating age and investment amount as per the requirements

### Function to validate age is between 0 and 65 ###
def validate_age(age):
    
    if age < 0 or age > 65:
        return False
    else:
        return True
        
### Function to validate investment amount is more than $5000 ###
def validate_investmentAmount(investmentAmount):
    
    if investmentAmount < 5000:
        return False
    else:
        return True