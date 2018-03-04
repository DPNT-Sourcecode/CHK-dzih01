
prices = {'A': {1: 50, 3: 130},
          'B': {1: 30, 2: 45},
          'C': {1: 20},
          'D': {1: 15}}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    ticket = {}
    total = 0

    if not skus:
        return -1

    for sku in skus:
        if sku in prices:
            ticket[sku] = ticket.get(sku, 0) + 1
        else:
            return -1

    print repr(ticket)

    for sku in ticket:
        for offer in sorted(prices[sku], reverse=True):
            times = ticket[sku] / offer
            # print "times: " + repr(ticket[sku]) + "/" + repr(offer) + " => " + repr(times)
            total += times * prices[sku][offer]
            ticket[sku] -= times * offer
    return total


if __name__ == "__main__":
    print repr(checkout('BBCB'))
