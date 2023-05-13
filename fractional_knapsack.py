def fractional_knapsack():
    max_weight = int(input("Input the maximum weight of the knapsack: "))

    benefits = input("Input the benefits of the items: ").split()
    weights = input("Input the weights of the items: ").split()

    if len(benefits) != len(weights):
        raise Exception("The number of benefits and weights must be the same.")

    weights = [int(i) for i in weights]
    benefits = [int(i) for i in benefits]
    num_items = len(weights)
    ratio = [i / j for i, j in zip(benefits, weights)]

    pack = []

    for i in range(num_items):
        most_valuable = max(ratio)
        index = ratio.index(most_valuable)
        if max_weight == 0:
            break
        elif max_weight >= weights[index]:
            pack.append((index + 1, weights[index]))
            max_weight -= weights[index]
            ratio[index] = 0
        else:
            pack.append((index + 1, max_weight))
            max_weight = 0
            break

    value = 0
    for i, j in enumerate(pack):
        if i < len(pack) - 1:
            value += benefits[j[0] - 1]
        else:
            value += benefits[j[0] - 1] * j[1] / weights[j[0] - 1]

    print(f'\nItem(s) selected (item, taken weight): {pack}\n')
    print(f'\nMaximum benefit: {value}\n')
