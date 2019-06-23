from heapq import heappush, heappop


def add_number(number_to_add, below, above):
    if not above or number_to_add > above[0]:
        heappush(above, number_to_add)
    else:
        heappush(below, -number_to_add)


def rebalance(lowers, highers):
    if len(lowers) - len(highers) > 1:
        heappush(highers, -heappop(lowers))
    elif len(highers) - len(lowers) > 1:
        heappush(lowers, -heappop(highers))


def get_median(lowers, highers):
    if len(lowers) == len(highers):
        return (-lowers[0] + highers[0])/2
    elif len(lowers) > len(highers):
        return -lowers[0]
    else:
        return highers[0]

def calc_median(input):

    below = []
    above = []

    for i in input:
        add_number(i, below, above)
        rebalance(below, above)

    return get_median(below, above)

def main():
    sample_imput = [12, 4, 5, 3, 8, 7]
    med = calc_median(sample_imput)
    print(med)


if __name__ == "__main__": main()