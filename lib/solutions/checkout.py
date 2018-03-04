
prices = {'A': {1: 50, 3: 130}
          'B': {1: 30, 2: 45}
          'C': {1: 20}
          'D': {1: 15}}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    ticket = {}

    for sku in skus:
        ticket.setdefault(sku, )



# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+