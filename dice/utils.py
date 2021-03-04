from rng import get_random_bytes

def roll_dice(sides=6):
    """ return 1 ... sides """
    d = get_random_bytes(1)
    print (sides)
    print (d)
    return 1+int.from_bytes(d, 'big') % sides
