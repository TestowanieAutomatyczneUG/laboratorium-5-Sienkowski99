def roman(num):
    symbols = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
    result = ""
    if num <= 10:
        return symbols[num]
    elif num <40:
        result += "X" * (num // 10) + symbols[num % 10]
    elif num < 50:
        result += "XL" + symbols[num % 10]
    elif num < 90:
        result += "L" + "X" * ((num - 50) // 10) + symbols[num % 10]
    return result