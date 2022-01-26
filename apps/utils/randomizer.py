from random import randint

def random_N_digit(n: int, type: str):
    range_start = 10**(n-1)
    range_end = (10**n)-1

    if type == 'idno':
        return 30000000000000000+randint(range_start, range_end)

    return randint(range_start, range_end)