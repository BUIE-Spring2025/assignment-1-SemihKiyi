def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    
    
    num2 =""
    if num > 3999 or 0>= num or num % 1 !=0:

        return None

    if num >= 1000:
        num2 += "M" * (num // 1000)
        num %= 1000

    if num >= 900:
        num2 += "CM"
        num -= 900
    
    if num >= 500:
        num2 += "D"
        num -= 500 

    if num >= 400:
        num2 += "CD"
        num -= 400 

    if num >= 100:
        num2 += "C" * (num // 100)
        num %= 100

    if num >= 90:
        num2 += "XC"
        num -= 90

    if num >= 50:
        num2 += "L"
        num -= 50

    if num >= 40:
        num2 += "XL"
        num -= 40

    if num >= 10:
        num2 += "X" * (num // 10)
        num %= 10

    if num >= 9:
        num2 += "IX"
        num -= 9

    if num >= 5:
        num2 += "V"
        num -= 5

    if num >= 4:
        num2 += "IV"
        num -= 4

    if num >= 1:
        num2 += "I" * num

    return num2


    
