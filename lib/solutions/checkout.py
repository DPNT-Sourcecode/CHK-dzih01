
prices = {'A': {1: 50, 3: 130},
          'B': {1: 30, 2: 45},
          'C': {1: 20},
          'D': {1: 15}}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    ticket = {}
    total = 0

    if skus is None:
        return -1

    for sku in skus:
        if sku in prices:
            ticket[sku] = ticket.get(sku, 0) + 1
        else:
            return -1

    for sku in ticket:
        print sku + " - " + repr(ticket[sku])
        for offer in sorted(prices[sku], reverse=True):
            print repr(ticket[sku]) + " / " + repr(prices[sku][offer])
            times = ticket[sku] / prices[sku][offer]
            print repr(times)
            total += times * offer
            print repr(offer)
            ticket[sku] -= times * offer
    
    return total


if __name__ == "__main__":
    checkout('AC')
