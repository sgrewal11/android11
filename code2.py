import re

def namecheck(s):
    """
    Checks if a name only includes alphabetic characters, hyphens, or single quotes.
    Names must be between 2 and 40 characters long.
    Quoted strings and double hyphens are disallowed.
    """
    # Define the regex pattern for valid names
    name_pattern = r"^[a-zA-Z][a-zA-Z'-]{1,39}$"
    
    # Check if the name matches the pattern
    if re.match(name_pattern, s):
        # Check for disallowed quoted strings and double hyphens
        if re.search(r"'.*'", s) or re.search(r"--", s):
            return False
        else:
            return True
    else:
        return False

# Example usage
print(namecheck("John-Doe"))   # True
print(namecheck("O'Connor"))   # True
print(namecheck("Anna-Maria")) # True
print(namecheck("Anna--Maria")) # False
print(namecheck("John 'Doe'")) # False
print(namecheck("J"))          # False
print(namecheck("ThisNameIsWayTooLongToBeValid")) # False
