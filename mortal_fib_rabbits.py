def mortal_fib(n_months: int, lifespan_months: int):
    if n_months == 1 or n_months == 2:
        return 1
    elif n_months <= lifespan_months:
        # if in prime of life, have offspring
        return mortal_fib(n_months - 1, lifespan_months) + mortal_fib(n_months - 2, lifespan_months)
    elif n_months == lifespan_months + 1:
        # if n_months alive is equal to lifespan, a rabbit dies.
        return mortal_fib(n_months - 1, lifespan_months) + mortal_fib(n_months - 2, lifespan_months) - 1
    else:
        # removes the dead rabbits from the total count but keeps alive rabbits
        return mortal_fib(n_months - 1, lifespan_months) + mortal_fib(n_months - 2, lifespan_months) - \
               mortal_fib(n_months - (lifespan_months + 1), lifespan_months)


def main():
    n_months = 6
    lifespan_months = 3
    print(n_months, mortal_fib(n_months, lifespan_months))


if __name__ == "__main__":
    main()
