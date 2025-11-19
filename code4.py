# Simulated external service call to check credit rating
def check_credit_rating(name, postcode, dob):
    # Simulating a response from an external credit rating service
    # Format: [name, postcode, dob, credit_score, return_code]
    return [name, postcode, dob, 550, 0]  # Example response with success

# Function to handle normal processing when credit check is successful
def do_normal_processing(cr):
    print(f"Credit check successful for {cr[0]} with a credit score of {cr[3]}.")

# Function to handle exception processing if something goes wrong
def do_exception_processing(cr, name, postcode, dob, failure_type):
    if failure_type == True:
        print(f"Request failure for {name}. Please check the service or inputs.")
    elif failure_type == False:
        print(f"Assertion error for {name}. Data mismatch or invalid rating.")

# Main function that checks the credit score
def credit_checker(name, postcode, dob):
    NAME = 0
    POSTCODE = 1
    DOB = 2
    RATING = 3
    RETURNCODE = 4
    REQUEST_FAILURE = True
    ASSERTION_ERROR = False
    
    # Initialize with a default "failure" result
    cr = ['', '', '', -1, 2]
    
    # Simulate call to the external service
    cr = check_credit_rating(name, postcode, dob)
    
    try:
        # Check that the response matches expected values and return code is valid
        assert cr[NAME] == name and cr[POSTCODE] == postcode and cr[DOB] == dob and \
               (0 <= cr[RATING] <= 600) and (0 <= cr[RETURNCODE] <= 2)
        
        # If return code is 0, the service call was successful
        if cr[RETURNCODE] == 0:
            do_normal_processing(cr)
        else:
            # If the return code is not 0, handle as a failure
            do_exception_processing(cr, name, postcode, dob, REQUEST_FAILURE)
    except AssertionError:
        # Handle any assertion errors (data mismatch, invalid results)
        do_exception_processing(cr, name, postcode, dob, ASSERTION_ERROR)

# Example call to the function
credit_checker("John Doe", "12345", "1990-01-01")
