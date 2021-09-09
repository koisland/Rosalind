from functools import cache


def loop():
    total_pop = [0]
    for month in range(1, 34):  # n here
        total_pop.append(return_pop(month, total_pop))
    print(total_pop[-1])


@cache
def return_pop(month, total_pop):
    if month == 1 or month == 2:
        return 1
    elif month >= 3:
        return total_pop[month - 1] + total_pop[month - 2] * 3  # k here
        # Starting at 3 months.
        # Previous month's rabbit pairs (-2) becomes adults and reproduce.
        # The previous immature generation is added in (-1) term.


loop()
