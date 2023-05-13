def dynamic_selection(W, B, T, max_weight, num_items, ptb):
    ptb.field_names = [k for k in range(max_weight + 1)]
    ptb.add_row([0 for i in range(max_weight + 1)])
    for i in range(1, num_items + 1):
        for j in range(1, max_weight + 1):
            if W[i] <= j:
                T[i][j] = max(T[i - 1][j], B[i] + T[i - 1][j - W[i]])
            else:
                T[i][j] = T[i - 1][j]
        ptb.add_row(T[i])
    fieldname = 'Items\\Weight'
    ptb._field_names.insert(0, fieldname)
    ptb._align[fieldname] = 'c'
    ptb._valign[fieldname] = 't'
    for i, _ in enumerate(ptb._rows):
        ptb._rows[i].insert(0, i)


def trace_back(i, j, W, B, S, T, ptb):
    if i == 0:
        print("\nItem(s) selected: ", end="")
        for k in range(1, len(W)):
            if S[k] == 1:
                print(k, end=" ")
        print("\n\nMaximum benefit: " + str(T[-1][-1]) + "\n")
        print(ptb)
        return

    if T[i][j] == T[i - 1][j]:
        trace_back(i - 1, j, W, B, S, T, ptb)
    elif T[i][j] == T[i - 1][j - W[i]] + B[i]:
        S[i] = 1
        trace_back(i - 1, j - W[i], W, B, S, T, ptb)
