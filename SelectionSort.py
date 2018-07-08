
def selection_sort(lst_sort):
    for i in range(0, len(lst_sort)):
        min_index = i
        for j in range(i + 1, len(lst_sort)):
            if lst_sort[j] < lst_sort[min_index]:
                min_index = j

        temp = lst_sort[i]
        lst_sort[i] = lst_sort[min_index]
        lst_sort[min_index] = temp

    return lst_sort


if __name__ == '__main__':

    list_to_sort = [9, 4, 6, 1, 8, 5, 2, 7, 3]

    list_to_sort = selection_sort(list_to_sort)

    print(list_to_sort)