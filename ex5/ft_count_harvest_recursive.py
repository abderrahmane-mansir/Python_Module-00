def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def rec(day):
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        rec(day + 1)
    rec(1)
