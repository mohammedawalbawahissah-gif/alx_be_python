import sys

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            return "Error: Division by zero"
        return num / den
    except ValueError:
        return "Error: Invalid number format"

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
