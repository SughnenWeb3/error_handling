# ===== TASK 2: Email Validator =====
# Create a custom InvalidEmailError exception
# The function should validate email format and raise InvalidEmailError if:
# - Email doesn't contain exactly one '@' symbol
# - Email doesn't contain at least one '.' after the '@'
# If input is empty, raise ValueError with message "Error: email cannot be empty"
# Keep asking until a valid email is entered

print("=== Task 2: Email Validator ===")
print("Email must contain '@' and a domain with '.'\n")
class InvalidEmailError(Exception):
    pass
def validate_email(prompt):
    while True:
        try:
            user_email = input(prompt).strip()
            if not user_email:
                raise ValueError("Error: email cannot be empty")
            if email.count('@') > 1:
                raise InvalidEmailError("Email must contain exactly one '@'")
            spec_index = email.index('@')
            if '.' not in email[spec_index:]:
                raise InvalidEmailError("Email must contain '.' after '@'")
            return email
        except (ValueError, InvalidEmailError) as email_error:
            print("Error has occured", email_error)
    #
    # Write your code here.
    # Define InvalidEmailError class
    # Validate email format
    # Handle exceptions and keep prompting
    #
    pass

email = validate_email("Enter your email: ")
print(f"Email accepted: {email}")
print()
