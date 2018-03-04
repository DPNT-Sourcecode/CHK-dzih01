
prices = {'A': {1: 50, 3: 130, 5: 200},
          'B': {1: 30, 2: 45},
          'C': {1: 20},
          'D': {1: 15},
          'E': {1: 40, 2: 'one_free'}}

# noinspection PyUnusedLocal


# skus = unicode string
def checkout(skus):
    ticket = {}
    total = 0

    if not skus:
        return total

    for sku in skus:
        if sku in prices:
            ticket[sku] = ticket.get(sku, 0) + 1
        else:
            return -1

    for sku in ticket:
        for offer in sorted(prices[sku], reverse=True):
            if prices[sku][offer] == 'one_free':
                times = ticket[sku] / offer
                total += times * offer * prices[sku][1]
                ticket[sku] -= times * (1 + offer)
            else:
                times = ticket[sku] / offer
                total += times * prices[sku][offer]
                ticket[sku] -= times * offer
            
            if ticket[sku] < 0:
                ticket[sku] = 0
    
    return total



