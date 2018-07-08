
def insertion_sort(lst_sort):

    for i in range(1, len(lst_sort)):
        index = i
        value = lst_sort[i]

        while index > 0 and lst_sort[index - 1] > value:
            lst_sort[index] = lst_sort[index - 1]
            index = index - 1
        lst_sort[index] = value
    return lst_sort


if __name__ == '__main__':

    list_to_sort = [9, 4, 6, 1, 8, 5, 2, 7, 3]

    list_to_sort = insertion_sort(list_to_sort)

    print(list_to_sort)