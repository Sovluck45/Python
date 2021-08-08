from functools import reduce

n_list = [el for el in range(100, 1001) if el % 2 == 0]


def calc_func(prev_el, el):
    return prev_el * el


print("Результат вычислений: ", reduce(calc_func, n_list))
