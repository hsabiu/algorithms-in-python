
def bubble_sort(lst_sort):

    for i in range(0, len(lst_sort) - 1):
        flag = False
        for j in range(0, len(lst_sort) - i - 1):
            if lst_sort[j] > lst_sort[j + 1]:
                temp = lst_sort[j + 1]
                lst_sort[j + 1] = lst_sort[j]
                lst_sort[j] = temp
                flag = True
        if not flag:
            break
    return lst_sort


if __name__ == '__main__':

    list_to_sort = [9, 4, 6, 1, 8, 5, 2, 7, 3]

    list_to_sort = bubble_sort(list_to_sort)

    print(list_to_sort)