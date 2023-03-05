
def bubble_s(lst_n: list):
    n = len(lst_n)-1

    while n > 0:
        for i in range(n):
            if lst_n[i] > lst_n[i+1]:
                lst_n[i], lst_n[i+1] = lst_n[i+1], lst_n[i]
        n -= 1
    return lst_n


print(bubble_s([1,2,53,532,52,224,6632,2141]))
