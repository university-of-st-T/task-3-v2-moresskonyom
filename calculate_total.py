from decimal import Decimal


def calculate_total(prices, *discounts, **options):
    s = Decimal(sum(prices))
    for i in discounts:
        s *= (100 - i) * Decimal(0.01)
    tax = options.get("tax")
    if tax != None:
        s *= (100 + tax) * Decimal(0.01)
    rd = options.get("round_to")
    if rd != None:
        s = round(s, rd)
    return float(s)


