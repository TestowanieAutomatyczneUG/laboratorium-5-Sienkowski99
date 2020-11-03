def roman(num):
    symbols = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
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
    helper.reverse()
    print(helper)
    result = ""
    for symbol in helper:
        while num >= symbol:
            result += symbols[symbol]
            num -= symbol
    return result
