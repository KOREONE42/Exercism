def say(number):
    if not (0 <= number <= 999_999_999_999):
        raise ValueError("input out of range")

    units = [
        "zero", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]
    
    scales = ["", "thousand", "million", "billion"]

    def convert_hundreds(n):
        if n == 0:
            return ""
        elif n < 20:
            return units[n]
        elif n < 100:
            return tens[n // 10] + ("-" + units[n % 10] if n % 10 != 0 else "")
        else:
            remainder = n % 100
            return (
                units[n // 100] + " hundred"
                + (" " + convert_hundreds(remainder) if remainder else "")
            )

    # Special case for zero
    if number == 0:
        return "zero"

    # Break the number into chunks of 3 digits
    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000

    # Build English phrase
    parts = []
    for idx, chunk in enumerate(chunks):
        if chunk != 0:
            words = convert_hundreds(chunk)
            scale = scales[idx]
            if scale:
                parts.append(f"{words} {scale}")
            else:
                parts.append(words)

    return " ".join(reversed(parts))
