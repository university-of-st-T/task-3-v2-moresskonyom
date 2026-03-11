def calculate_total(prices, *discounts, **options):
    s = sum(prices)
    for i in discounts:
        s *= (100 - i) * 0.01
    tax = options.get("tax")
    if tax != None:
        s *= (100 + tax) * 0.01
    rd = options.get("round_to")
    if rd != None:
        s = round(s, rd)
    return s
