
prices = {'A': {1: 50, 3: 130}
          'B': {1: 30, 2: 45}
          'C': {1: 20}
          'D': {1: 15}}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    ticket = {}
    total = 0

    for sku in skus:
        ticket[sku] = ticket.get(sku, 0) + 1

    for sku in ticket:
        for offer in sorted(prices[sku], reversed=True)
            times = ticket[sku] / prices[sku]:
            total += times * offer
            ticket[sku] -= times * offer
        else:    
