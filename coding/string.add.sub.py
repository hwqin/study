
def add_large_numbers_with_sign(num1_str, num2_str):
    """Adds two large numbers (with optional signs) represented as strings."""
    sign1 = -1 if num1_str.startswith('-') else 1
    sign2 = -1 if num2_str.startswith('-') else 1
    mag1_str = num1_str[1:] if sign1 == -1 else num1_str
    mag2_str = num2_str[1:] if sign2 == -1 else num2_str

    if sign1 == sign2:
        result_mag = add_large_numbers(mag1_str, mag2_str)
        return "-" + result_mag if sign1 == -1 and result_mag != '0' else result_mag
    else:
        if compare_magnitudes(mag1_str, mag2_str) >= 0:
            result_mag = subtract_large_numbers(mag1_str, mag2_str)
            return "-" + result_mag if sign1 == -1 and result_mag != '0' else result_mag
        else:
            result_mag = subtract_large_numbers(mag2_str, mag1_str)
            return "-" + result_mag if sign2 == -1 and result_mag != '0' else result_mag

def subtract_large_numbers_with_sign(num1_str, num2_str):
    """Subtracts two large numbers (with optional signs) represented as strings (num1 - num2)."""
    sign1 = -1 if num1_str.startswith('-') else 1
    sign2 = -1 if num2_str.startswith('-') else 1
    mag1_str = num1_str[1:] if sign1 == -1 else num1_str
    mag2_str = num2_str[1:] if sign2 == -1 else num2_str

    # Convert subtraction to addition based on signs
    if sign1 == 1 and sign2 == 1:  # a - b
        return subtract_large_numbers(mag1_str, mag2_str)
    elif sign1 == 1 and sign2 == -1: # a - (-b) = a + b
        return add_large_numbers_with_sign(mag1_str, mag2_str)
    elif sign1 == -1 and sign2 == 1: # -a - b = -(a + b)
        result_mag = add_large_numbers(mag1_str, mag2_str)
        return "-" + result_mag if result_mag != '0' else '0'
    elif sign1 == -1 and sign2 == -1: # -a - (-b) = -a + b = b - a
        return add_large_numbers_with_sign("-" + mag2_str, "-" + mag1_str) # Reuse addition logic

def compare_magnitudes(num1_str, num2_str):
    """Compares the magnitudes of two large numbers (strings).
    Returns 1 if num1 > num2, -1 if num1 < num2, and 0 if equal.
    """
    n1, n2 = len(num1_str), len(num2_str)
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        if num1_str > num2_str:
            return 1
        elif num1_str < num2_str:
            return -1
        else:
            return 0

# Helper functions (add_large_numbers and subtract_large_numbers from previous example)
def add_large_numbers(num1_str, num2_str):
    num1_str = num1_str.lstrip('0') or '0'
    num2_str = num2_str.lstrip('0') or '0'
    n1, n2 = len(num1_str), len(num2_str)
    if n1 < n2:
        num1_str = '0' * (n2 - n1) + num1_str
    elif n2 < n1:
        num2_str = '0' * (n1 - n2) + num2_str
    result = []
    carry = 0
    for i in range(len(num1_str) - 1, -1, -1):
        digit1 = int(num1_str[i])
        digit2 = int(num2_str[i])
        current_sum = digit1 + digit2 + carry
        result.append(str(current_sum % 10))
        carry = current_sum // 10
    if carry:
        result.append(str(carry))
    return "".join(result[::-1])

def subtract_large_numbers(num1_str, num2_str):
    num1_str = num1_str.lstrip('0') or '0'
    num2_str = num2_str.lstrip('0') or '0'
    if len(num1_str) < len(num2_str) or (len(num1_str) == len(num2_str) and num1_str < num2_str):
        return "-" + subtract_large_numbers(num2_str, num1_str)
    n1, n2 = len(num1_str), len(num2_str)
    num2_str = '0' * (n1 - n2) + num2_str
    result = []
    borrow = 0
    for i in range(n1 - 1, -1, -1):
        digit1 = int(num1_str[i])
        digit2 = int(num2_str[i])
        current_diff = digit1 - digit2 - borrow
        if current_diff < 0:
            current_diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(current_diff))
    result_str = "".join(result[::-1]).lstrip('0')
    return result_str if result_str else '0'

# Example Usage with Signs
num1_signed = "-12345"
num2_signed = "6789"
sum_signed = add_large_numbers_with_sign(num1_signed, num2_signed)
print(f"Sum of {num1_signed} and {num2_signed}: {sum_signed}")

num3_signed = "100"
num4_signed = "-50"
diff_signed = subtract_large_numbers_with_sign(num3_signed, num4_signed)
print(f"Difference of {num3_signed} and {num4_signed}: {diff_signed}")

num5_signed = "-200"
num6_signed = "-100"
diff_signed_negative = subtract_large_numbers_with_sign(num5_signed, num6_signed)
print(f"Difference of {num5_signed} and {num6_signed}: {diff_signed_negative}")