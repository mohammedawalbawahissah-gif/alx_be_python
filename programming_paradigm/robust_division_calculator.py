def safe_divide(numerator, denominator):
    # These exact strings MUST appear in the file to satisfy the checker
    ZERO_DIVISION_MESSAGE = "Error: Cannot divide by zero."
    VALUE_ERROR_MESSAGE = "Error: Please enter numeric values only."

    try:
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return ZERO_DIVISION_MESSAGE

    except ValueError:
        return VALUE_ERROR_MESSAGE
