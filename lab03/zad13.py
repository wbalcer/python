def sort_numbers(numbers, ascending=True):
    return sorted(numbers, reverse=not ascending)

numbers_list = [4, 2, 9, 1, 5, 6]
direction = input("Podaj kierunek sortowania (asc/desc): ").strip().lower()
ascending_order = direction == "asc"

sorted_list = sort_numbers(numbers_list, ascending_order)
print("Posortowana lista:", sorted_list)