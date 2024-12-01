# Validate phone number
def validate_phone(phone):
    if not phone.isdigit():
        print("\nError: Phone number must contain only digits.")
        return False
    return True

# Validate email
def validate_email(email):
    if '@' not in email or '.' not in email:
        print("\nError: Email must contain '@' and '.'")
        return False
    return True
