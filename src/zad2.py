def roman(num):
    symbols = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XV",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    helper = []
    for key in symbols:
        helper.append(key)
    print(helper)
    result = ""
    if num in symbols:
        result = symbols[num]
    if num <= 10:
        return symbols[num]
    elif num <40:
        result += "X" * (num // 10) + symbols[num % 10]
    elif num < 50:
        result += "XL" + symbols[num % 10]
    elif num < 90:
        result += "L" + "X" * ((num - 50) // 10) + symbols[num % 10]
    elif num < 100:
        result += "XC" + "X" * ((num - 90) // 10) + symbols[num % 10]
    return result