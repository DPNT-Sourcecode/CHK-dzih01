
# prices = {'A': {1: 50, 3: 130, 5: 200},
#           'B': {1: 30, 2: 45},
#           'C': {1: 20},
#           'D': {1: 15},
#           'E': {1: 40, 2: 'one_free'},
#           'F': {1: 10, 2: 'one_free'}}

prices = {'A': {1: 50, 3: 130, 5: 200},
          'B': {1: 30, 2: 45},
          'C': {1: 20},
          'D': {1: 15},
          'E': {1: 40, 2: {'offer': 'one_free',
                           'over': 'B'}},
          'F': {1: 10, 2: {'one_free',
                           'over': 'F'}}}


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

    for sku in sorted(ticket, reverse=True):
        for offer in sorted(prices[sku], reverse=True):
            if prices[sku][offer] == 'one_free':
                times = ticket[sku] / offer
                total += times * offer * prices[sku][1]
                ticket[sku] -= times * offer
                
                if sku == 'E' and ticket.get('B'):
                    ticket['B'] -= times
                    if ticket['B'] < 0:
                        ticket['B'] = 0
                
                if sku == 'F' and ticket.get('F'):
                    ticket['F'] -= times
                    if ticket['F'] < 0:
                        ticket['F'] = 0

            else:
                times = ticket[sku] / offer
                total += times * prices[sku][offer]
                ticket[sku] -= times * offer

            if ticket[sku] < 0:
                ticket[sku] = 0

    return total
