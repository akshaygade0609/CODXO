def currency_converter(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

amount = float(input("Enter amount in USD: "))
exchange_rate = float(input("Enter exchange rate: "))

converted_amount = currency_converter(amount, exchange_rate)
print("Converted amount:", converted_amount)