PRICES = {'A': {1: 50, 3: 130, 5: 200},
          'B': {1: 30, 2: 45},
          'C': {1: 20},
          'D': {1: 15},
          'E': {1: 40, 2: {'offer': 'one_free',
                           'over': 'B'}},
          'F': {1: 10, 2: {'offer': 'one_free',
                           'over': 'F'}},
          'G': {1: 20},
          'H': {1: 10, 5: 45, 10: 80},
          'I': {1: 35},
          'J': {1: 60},
          'K': {1: 70, 2: 120},
          'L': {1: 90},
          'M': {1: 15},
          'N': {1: 40, 3: {'offer': 'one_free',
                           'over': 'M'}},
          'O': {1: 10},
          'P': {1: 50, 5: 200},
          'Q': {1: 30, 3: 80},
          'R': {1: 50, 3: {'offer': 'one_free',
                           'over': 'Q'}},
          'S': {1: 20, 3: {'offer': 'buy_any_three',
                           'over':  ['S', 'T', 'X', 'Y', 'Z'],
                           'group_price': 45}},
          'T': {1: 20, 3: {'offer': 'buy_any_three',
                           'over':  ['S', 'T', 'X', 'Y', 'Z'],
                           'group_price': 45}},
          'U': {1: 40, 3: {'offer': 'one_free',
                           'over': 'U'}},
          'V': {1: 50, 2: 90, 3: 130},
          'W': {1: 20},
          'X': {1: 17, 3: {'offer': 'buy_any_three',
                           'over':  ['S', 'T', 'X', 'Y', 'Z'],
                           'group_price': 45}},
          'Y': {1: 20, 3: {'offer': 'buy_any_three',
                           'over':  ['S', 'T', 'X', 'Y', 'Z'],
                           'group_price': 45}},
          'Z': {1: 21, 3: {'offer': 'buy_any_three',
                           'over':  ['S', 'T', 'X', 'Y', 'Z'],
                           'group_price': 45}}}


GROUP_OFFER = ['S', 'T', 'X', 'Y', 'Z']


def apply_group_offers(ticket):
    products = {}
    num_products = 0
    for sku in GROUP_OFFER:
        if ticket.get(sku):
            products[sku] = ticket[sku]
            num_products += ticket[sku]
    
    times = num_products / 3
    while times:
        for sku in products:
            if products[sku] >= times:
                products[sku] -= times  
                times = 0 
            else:
                products[sku] = 0
                times -= products[sku] 


    
    return total, ticket


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    ticket = {}
    total = 0

    if not skus:
        return total

    for sku in skus:
        if sku in PRICES:
            ticket[sku] = ticket.get(sku, 0) + 1
        else:
            return -1

    apply_group_offers(ticket)

    for sku in sorted(ticket, reverse=True):
        for offer in sorted(PRICES[sku], reverse=True):
            if type(PRICES[sku][offer]) == dict:
                if PRICES[sku][offer]['offer'] == 'one_free':
                    while ticket[sku] >= offer:
                        total += offer * PRICES[sku][1]
                        ticket[sku] -= offer

                        offer_over = PRICES[sku][offer]['over']
                        if ticket.get(offer_over):
                            ticket[offer_over] -= 1
                            if ticket[offer_over] < 0:
                                ticket[offer_over] = 0

            else:
                times = ticket[sku] / offer
                total += times * PRICES[sku][offer]
                ticket[sku] -= times * offer

            if ticket[sku] < 0:
                ticket[sku] = 0

    return total
